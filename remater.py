import json
import os
import requests
import time
from urllib.request import urlretrieve

results = []
thumbnails = []
image_count = 0
topic_id = "8807683"
basic_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_new?topic_id=" + topic_id
history_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?"


def download(order):
    for combined_item in order:
        count = 0
        if not os.path.exists("images"):
            os.mkdir("images")

        for url in combined_item["images"]:
            count += 1
            if len(combined_item["images"]) == 1:
                counter = ""
            else:
                counter = " " + str(count)
            file_extend_name = url[url.rfind("."):]
            file_name = combined_item["name"] + " " + combined_item['time'] + counter + file_extend_name
            path = os.path.abspath("images")
            full_name = os.path.join(path, file_name)
            urlretrieve(url, full_name)


def dumper(xhr, num, thumbnail=False):
    global results, thumbnails, image_count

    xhr_data = xhr["data"]
    offset = xhr_data['offset']
    for source in xhr_data['cards']:
        if image_count >= num:
            break
        card = json.loads(source["card"])
        try:
            images_temp = []
            thumbnail_temp = []
            for picture in card["item"]["pictures"]:
                if image_count >= num:
                    break
                img_src = picture["img_src"]
                images_temp.append(img_src)
                if thumbnail:
                    img_thumbnail = img_src + "@104w_104h.webp"
                    thumbnail_temp.append(img_thumbnail)
                image_count += 1
            user_name = card['user']['name']
            timestamp = card['item']['upload_time']
            upload_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(timestamp))
            profile = {
                'name': user_name,
                'images': images_temp,
                'time': upload_time
            }
            thumbnail_profile = {
                'images': thumbnail_temp
            }
            results.append(profile)
            thumbnails.append(thumbnail_profile)
        except KeyError:
            pass
    if image_count < num:
        history_url = history_api_url + "topic_id=" + topic_id + "&offset_dynamic_id=" + offset
        history = requests.get(history_url).json()
        if thumbnail:
            dumper(history, num, True)
        else:
            dumper(history, num)


def main():
    web = requests.get(basic_api_url)
    xhr = web.json()
    try:
        number = int(input("数量？ "))
    except ValueError:
        print("请输入正确的数量")
        exit()
    dumper(xhr, number)


def interface(number):
    global results, image_count, thumbnails
    results = []
    thumbnails = []
    image_count = 0
    web = requests.get(basic_api_url)
    xhr = web.json()
    dumper(xhr, number, thumbnail=True)
    return [thumbnails, results]


if __name__ == "__main__":
    main()
    download(results)
# print(results)
# count = 0
# for item in results:
#     print("name", item["name"])
#     print("images", item["images"])
#     count += len(item["images"])
# print(count)
