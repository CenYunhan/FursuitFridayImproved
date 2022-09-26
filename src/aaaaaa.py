import atexit
import dataclasses
import json
import os
import shutil
import tempfile
import time
from datetime import datetime
from typing import List, Tuple, Union

import requests

API_TEMPLATE: str = 'https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?topic_id={topic_id}&offset_dynamic_id={offset}'
REQUEST_TIME_INTERVAL: float = 7.0


@dataclasses.dataclass(frozen=True)
class ImagePostInfo:
    '''
    数据类，记录各个图片动态中的所需信息，包括发布者的用户名、发布时间及各图片链接。
    '''
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
        self.last_request_time: float = time.monotonic() - REQUEST_TIME_INTERVAL

    def __fetch_topic_data(self) -> requests.Response:
        '''通过发送HTTPS请求获取数据'''
        if not self.has_more:  # 当获取完指定话题的所有动态时
            raise StopIteration  # 结束迭代
        # 对每次请求的时间间隔进行限制，避免短时间内发出大量请求导致IP被风控
        if (time_interval := time.monotonic() - self.last_request_time) < REQUEST_TIME_INTERVAL:
            time.sleep(REQUEST_TIME_INTERVAL - time_interval)
        self.last_request_time = time.monotonic()  # 记录最后一次发送HTTPS请求的时间
        # TODO 处理ConnectionError
        return requests.get(API_TEMPLATE.format(topic_id=self.topic_id, offset=self.offset))

    def __parse_post_list(self, response: requests.Response) -> List[ImagePostInfo]:
        '''解析动态列表'''
        data: dict = response.json()  # 解析服务器回应的JSON数据
        # TODO 处理data['code']非0的情况
        self.has_more = bool(data['data']['has_more'])  # 判断是否还有剩余动态
        post_list: List[ImagePostInfo] = []
        for post_info in data['data']['cards']:
            if post_info['desc']['type'] == 2:  # 当前动态为图片动态时
                post_details: dict = json.loads(post_info['card'])
                post_list.append(
                    ImagePostInfo(
                        post_details['user']['name'],
                        datetime.strftime(datetime.fromtimestamp(post_details['item']['upload_time']), r'%Y-%m-%d %H:%M:%S'),
                        tuple(pic_info['img_src'] for pic_info in post_details['item']['pictures'])  # type: ignore[arg-type]
                    )
                )
        self.offset = data['data']['offset']
        return post_list

    def __iter__(self) -> 'PostListPraser':
        return self

    def __next__(self) -> List[ImagePostInfo]:
        return self.__parse_post_list(self.__fetch_topic_data())


@dataclasses.dataclass(frozen=True)
class ImageInfo:
    '''
    数据类，记录各图片的相关信息，包括发布者的用户名、发布时间、图片链接及缩略图路径。
    '''
    user_name: str
    post_time: str
    image_uri: str
    thumbnail_path: str


class ImageContainer:
    '''
    容器，用于下载缩略图及储存图片信息。
    '''
    def __init__(self) -> None:
        self.__tmp_dir_path: str = tempfile.mkdtemp()  # 创建缓存文件夹
        atexit.register(shutil.rmtree, self.__tmp_dir_path)  # 在程序退出时移除缓存文件夹
        self.__data: List[ImageInfo] = []

    def __len__(self) -> int:
        return len(self.__data)

    def __getitem__(self, key: Union[int, slice]) -> Union[ImageInfo, List[ImageInfo]]:
        return self.__data[key]

    def __download_thumbnail(self, uri: str) -> str:
        '''下载URI对应图片的缩略图'''
        thumbnail_path: str = os.path.join(self.__tmp_dir_path, 'thmb_' + os.path.split(uri)[-1])
        with open(thumbnail_path, 'wb') as file:
            # TODO 处理ConnectionError
            file.write(requests.get(uri + '@104w_104h').content)
        return thumbnail_path

    def append(self, post_info: ImagePostInfo, /) -> None:
        for uri in post_info.image_uris:
            self.__data.append(
                ImageInfo(
                    post_info.user_name,
                    post_info.post_time,
                    uri,
                    self.__download_thumbnail(uri)
                )
            )

    def _show(self) -> None:
        from pprint import pprint
        pprint(self.__data)


if __name__ == '__main__':
    from pprint import pprint
    x = PostListPraser(8807683)
    c = ImageContainer()
    count = 3
    while count:
        print(f'count = {count}')
        lst = next(x)
        for img_post_info in lst:
            c.append(img_post_info)
        pprint(lst)
        print()
        count -= 1
    else:
        c._show()
    input()  # 阻塞线程
