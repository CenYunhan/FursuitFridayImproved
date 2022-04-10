import json
import os
import requests
from urllib.request import urlretrieve


def dumper(xhr, num):
    global result

    xhr_data = xhr["data"]
    offset = xhr_data['offset']
    for item in xhr_data['cards']:
        card = json.loads(item["card"])
        try:
            for picture in card["item"]["pictures"]:
                img_src = picture["img_src"]
                result.append(img_src)
        except KeyError:
            pass
    if len(result) > num:
        result = result[:num]
        pass
    else:
        history_url = history_api_url + "topic_id=" + topic_id + "&offset_dynamic_id=" + offset
        history = requests.get(history_url).json()
        dumper(history, num)

result = []
topic_id = "8807683"
basic_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_new?topic_id=" + topic_id
history_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?"
web = requests.get(basic_api_url)
xhr = web.json()
dumper(xhr, 30)
print(result)
for i in result:
    f = i[i.rfind("/") + 1:]
    print(f)
    urlretrieve(i, os.path.join(os.path.abspath("images"), f))
print(len(result), result)
