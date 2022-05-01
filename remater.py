import json
import os
import requests
from urllib.request import urlretrieve


def dumper(xhr, num):
    global results, image_count

    xhr_data = xhr["data"]
    offset = xhr_data['offset']
    for source in xhr_data['cards']:
        if image_count >= num:
            break
        card = json.loads(source["card"])
        try:
            images_temp = []
            for picture in card["item"]["pictures"]:
                if image_count >= num:
                    break
                img_src = picture["img_src"]
                images_temp.append(img_src)
                image_count += 1
            user_name = card['user']['name']
            profile = {
                'name': user_name,
                'images': images_temp
            }
            results.append(profile)
        except KeyError:
            pass
    if image_count < num:
        history_url = history_api_url + "topic_id=" + topic_id + "&offset_dynamic_id=" + offset
        history = requests.get(history_url).json()
        dumper(history, num)


results = []
topic_id = "8807683"
basic_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_new?topic_id=" + topic_id
history_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?"
web = requests.get(basic_api_url)
image_count = 0
xhr = web.json()
dumper(xhr, int(input("数量？ ")))
for item in results:
    for url in item["images"]:
        urlretrieve(url, os.path.abspath("images") + url[url.rfind("/"):])
# print(results)
# count = 0
# for item in results:
#     print("name", item["name"])
#     print("images", item["images"])
#     count += len(item["images"])
# print(count)
