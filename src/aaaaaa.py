import asyncio
import atexit
import dataclasses
import json
import os
import shutil
import tempfile
import time
from datetime import datetime
from typing import TYPE_CHECKING

from aiofiles import open as async_open
from aiohttp import ClientSession
from requests import get as requests_get

if TYPE_CHECKING:
    from typing import Any, Coroutine, List


API_TEMPLATE: str = 'https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?topic_id={topic_id}&offset_dynamic_id={offset}'
REQUEST_TIME_INTERVAL: float = 3.0


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

        # 协程
        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)
        self.event_loop.run_until_complete(self.__create_client_session())

        # 缓存文件夹
        self.__tmp_dir_path: str = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, self.__tmp_dir_path)

    def __del__(self) -> None:
        asyncio.set_event_loop(self.event_loop)
        self.event_loop.run_until_complete(self.__close_client_session())
        # TODO 下方语句在Python 3.10正常运行，在Python 3.8会引发RuntimeError，原因尚不明确
        # self.event_loop.close()

    def __iter__(self) -> 'ImageFetcher':
        return self

    def __next__(self) -> 'List[ImageInfo]':
        asyncio.set_event_loop(self.event_loop)
        # TODO 处理ConnectionError
        return self.event_loop.run_until_complete(self.__parse_post_list(self.__fetch_post_list()))

    async def __create_client_session(self) -> None:
        self.client_session: ClientSession = ClientSession()

    async def __close_client_session(self) -> None:
        await self.client_session.close()

    def __fetch_post_list(self) -> dict:
        if not self.has_more:
            raise StopIteration  # 结束迭代

        # 对每次请求的时间间隔进行限制，避免短时间内发出大量请求导致IP被风控
        if (time_interval := time.monotonic() - self.last_request_time) < REQUEST_TIME_INTERVAL:
            time.sleep(REQUEST_TIME_INTERVAL - time_interval)
        self.last_request_time = time.monotonic()

        # 向服务器发送HTTPS请求并解析
        return requests_get(API_TEMPLATE.format(topic_id=self.topic_id, offset=self.offset)).json()

    async def __parse_post_list(self, resp_data: dict) -> 'List[ImageInfo]':
        # TODO 处理data['code']非0的情况
        self.has_more = bool(resp_data['data']['has_more'])

        # 创建容纳Coroutine对象的列表
        coro_list: List['Coroutine[Any, Any, ImageInfo]'] = []

        # 第一层循环：遍历返回数据中的每条动态信息
        for post_info in resp_data['data']['cards']:
            # 判断是否为为图片动态
            if post_info['desc']['type'] == 2:
                # 解析当前动态的详细信息
                post_details: dict = json.loads(post_info['card'])
                # 转换当前动态的时间戳
                post_time: str = datetime.strftime(
                    datetime.fromtimestamp(post_details['item']['upload_time']),
                    r'%Y-%m-%d %H:%M:%S'
                )
                # 第二层循环：遍历当前动态中的每条图片信息
                for pic_info in post_details['item']['pictures']:
                    # 向列表中添加用于构造当前图片ImageInfo对象的Coroutine对象
                    coro_list.append(
                        self.__create_image_info(
                            post_details['user']['name'],
                            post_time,
                            pic_info['img_src']
                        )
                    )

        # 设置偏移量
        self.offset = resp_data['data']['offset']

        # 在已创建的event_loop中执行所有的Coroutine对象
        return await asyncio.gather(*coro_list)

    async def __create_image_info(self, user_name: str, post_time: str, image_uri: str) -> ImageInfo:
        thumbnail_path: str = os.path.join(self.__tmp_dir_path, 'thmb_' + os.path.split(image_uri)[-1])
        async with async_open(thumbnail_path, 'wb') as file:
            async with self.client_session.get(image_uri + '@104w_104h') as resp:
                await file.write(await resp.read())
        return ImageInfo(user_name, post_time, image_uri, thumbnail_path)


if __name__ == '__main__':
    start_time: float = time.monotonic()
    from pprint import pprint
    count = 1
    for x in ImageFetcher(8807683):
        print(f'count = {count}')
        pprint(x)
        print()
        if count >= 3:
            print(type(x), type(x[0]))
            break
        count += 1
    print('运行总时长：{0:.3f}秒'.format(time.monotonic() - start_time))
    input()  # 阻塞线程
