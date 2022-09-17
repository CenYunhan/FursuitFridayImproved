import dataclasses
import json
import time
from datetime import datetime
from typing import List, Tuple

import requests

API_TEMPLATE: str = 'https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?topic_id={topic_id}&offset_dynamic_id={offset}'
REQUEST_TIME_INTERVAL: float = 7.0


@dataclasses.dataclass(frozen=True)
class ImageInfo:
    user_name: str
    post_time: str
    image_uris: Tuple[str]


class PostListPraser:
    '''
    动态列表解析器：
        传入话题ID构造一个迭代器。
        每次对其进行迭代时，该迭代器会向服务器发送HTTPS请求并解析，当获取完指定话题的所有动态时结束迭代。
    '''
    def __init__(self, topic_id: int) -> None:
        self.topic_id: int = topic_id
        self.offset: int = 0
        self.has_more: bool = True
        self.last_request_time: float = time.monotonic()

    def __fetch_topic_data(self) -> requests.Response:
        '''通过发送HTTPS请求获取数据'''
        if not self.has_more:  # 当获取完指定话题的所有动态时
            raise StopIteration  # 结束迭代
        # TODO 处理ConnectionError
        # 对每次请求的时间间隔进行限制，避免短时间内发出大量请求导致IP被风控
        if (time_interval := time.monotonic() - self.last_request_time) < REQUEST_TIME_INTERVAL:
            time.sleep(REQUEST_TIME_INTERVAL - time_interval)
        self.last_request_time = time.monotonic()  # 记录最后一次发送HTTPS请求的时间
        return requests.get(API_TEMPLATE.format(topic_id=self.topic_id, offset=self.offset))

    def __parse_post_list(self, response: requests.Response) -> List[ImageInfo]:
        '''解析动态列表'''
        data: dict = response.json()  # 解析服务器回应的JSON数据
        # TODO 处理data['code']非0的情况
        self.has_more = bool(data['data']['has_more'])  # 判断是否还有剩余动态
        post_list: List[ImageInfo] = []
        for post_info in data['data']['cards']:
            if post_info['desc']['type'] == 2:  # 当前动态为图片动态时
                post_details: dict = json.loads(post_info['card'])
                post_list.append(
                    ImageInfo(
                        post_details['user']['name'],
                        datetime.strftime(datetime.fromtimestamp(post_details['item']['upload_time']), r'%Y-%m-%d %H:%M:%S'),
                        tuple(pic_info['img_src'] for pic_info in post_details['item']['pictures'])  # type: ignore[arg-type]
                    )
                )
        self.offset = data['data']['offset']
        return post_list

    def __iter__(self):
        return self

    def __next__(self):
        return self.__parse_post_list(self.__fetch_topic_data())


if __name__ == '__main__':
    from pprint import pprint
    x = PostListPraser(8807683)
    count = 5
    while count:
        print(f'count = {count}')
        pprint(next(x))
        print()
        count -= 1
