import atexit
import dataclasses
import json
import os
import shutil
import tempfile
import time
from datetime import datetime
from typing import List

import requests

API_TEMPLATE: str = 'https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?topic_id={topic_id}&offset_dynamic_id={offset}'
REQUEST_TIME_INTERVAL: float = 3.5


@dataclasses.dataclass(frozen=True)
class ImageInfo:
    '''
    数据类，记录各图片的相关信息，包括发布者的用户名、发布时间、图片链接及缩略图路径。
    '''
    user_name: str
    post_time: str
    image_uri: str
    thumbnail_path: str


class ImageFetcher:
    def __init__(self, topic_id: int) -> None:
        # 网络请求
        self.topic_id: int = topic_id
        self.offset: int = 0
        self.has_more: bool = True
        self.last_request_time: float = time.monotonic() - REQUEST_TIME_INTERVAL

        # 缓存文件夹
        self.__tmp_dir_path: str = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, self.__tmp_dir_path)

    def __iter__(self) -> 'ImageFetcher':
        return self

    def __next__(self) -> List[ImageInfo]:
        return self.__parse_post_list(self.__fetch_post_list())

    def __fetch_post_list(self) -> requests.Response:
        '''发送HTTPS请求获取话题当前偏移量的动态列表'''
        if not self.has_more:  # 当获取完指定话题的所有动态时
            raise StopIteration  # 结束迭代
        # 对每次请求的时间间隔进行限制，避免短时间内发出大量请求导致IP被风控
        if (time_interval := time.monotonic() - self.last_request_time) < REQUEST_TIME_INTERVAL:
            time.sleep(REQUEST_TIME_INTERVAL - time_interval)
        self.last_request_time = time.monotonic()  # 记录最后一次发送HTTPS请求的时间
        # TODO 处理ConnectionError
        return requests.get(API_TEMPLATE.format(topic_id=self.topic_id, offset=self.offset))

    def __parse_post_list(self, response: requests.Response) -> List[ImageInfo]:
        '''解析动态列表'''
        data: dict = response.json()  # 解析服务器回应的JSON数据
        # TODO 处理data['code']非0的情况
        self.has_more = bool(data['data']['has_more'])  # 检查是否还有剩余动态
        img_info_list: List[ImageInfo] = []
        for post_info in data['data']['cards']:  # 遍历当前动态列表中的每条动态
            if post_info['desc']['type'] == 2:  # 当前动态为图片动态时
                post_details: dict = json.loads(post_info['card'])  # 解析当前动态的详细信息
                post_time: str = datetime.strftime(
                    datetime.fromtimestamp(post_details['item']['upload_time']), r'%Y-%m-%d %H:%M:%S'
                )  # 转换时间戳为特定格式的时间表示
                for img_uri in (pic_info['img_src'] for pic_info in post_details['item']['pictures']):
                    img_info_list.append(
                        ImageInfo(
                            post_details['user']['name'],
                            post_time,
                            img_uri,
                            self.__download_thumbnail(img_uri)
                        )
                    )
        self.offset = data['data']['offset']  # 设置偏移量
        return img_info_list

    def __download_thumbnail(self, uri: str) -> str:
        '''下载URI对应图片的缩略图'''
        thumbnail_path: str = os.path.join(self.__tmp_dir_path, 'thmb_' + os.path.split(uri)[-1])
        with open(thumbnail_path, 'wb') as file:
            # TODO 处理ConnectionError
            file.write(requests.get(uri + '@104w_104h').content)
        return thumbnail_path  # 返回缩略图路径


if __name__ == '__main__':
    from pprint import pprint
    count = 1
    for x in ImageFetcher(8807683):
        print(f'count = {count}')
        pprint(x)
        print()
        if count >= 3:
            print(type(x))
            break
        count += 1
    input()  # 阻塞线程
