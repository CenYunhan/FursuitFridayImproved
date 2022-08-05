import json
import os
import requests
import time
from urllib.request import urlretrieve

results = []
thumbnails = []
names = []
names_without_ext = []
image_count = 0
topic_id = "8807683"
basic_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_new?topic_id="
history_api_url = "https://api.vc.bilibili.com/topic_svr/v1/topic_svr/topic_history?"


def download(order, return_name=False, no_ext_name=False):
    global names, names_without_ext
    names = []
    names_without_ext = []
    for combined_item in order:
        count = 0
        for url in combined_item["images"]:
            count += 1
            if len(combined_item["images"]) == 1:
                counter = ""
            else:
                counter = " " + str(count)
            file_extend_name = url[url.rfind("."):]
            file_name = combined_item["name"] + " " + combined_item['time'] + counter + file_extend_name

            if no_ext_name and return_name:
                file_name_without_ext = combined_item["name"] + " " + combined_item['time'] + counter
                names.append(file_name)
                names_without_ext.append(file_name_without_ext)
            else:
                if not os.path.exists("images"):
                    os.mkdir("images")
                path = os.path.abspath("images")
                full_name = os.path.join(path, file_name)
                # print(full_name)
                urlretrieve(url, full_name)


def dumper(xhr, num, thumbnail=False):
    global results, thumbnails, image_count

    xhr_data = xhr["data"]
    offset = xhr_data['offset']
    for source in xhr_data['cards']:
        if image_count >= num:
            break
        card = json.loads(source["card"])
        images_temp = []
        thumbnail_temp = []
        try:
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


def search_service(xhr, num, search_content):
    global results, thumbnails, image_count

    xhr_data = xhr["data"]
    offset = xhr_data['offset']

    for source in xhr_data['cards']:
        card = json.loads(source["card"])
        images_temp = []
        thumbnail_temp = []
        try:
            user_name = card['user']['name']
            if search_content == user_name:
                if image_count >= num:
                    break
                for picture in card["item"]["pictures"]:
                    img_src = picture["img_src"]
                    images_temp.append(img_src)
                    img_thumbnail = img_src + "@104w_104h.webp"
                    thumbnail_temp.append(img_thumbnail)
                    image_count += 1
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
        search_service(history, num, search_content)


def main():
    web = requests.get(basic_api_url + topic_id)
    xhr = web.json()
    try:
        number = int(input("数量？ "))
    except ValueError:
        print("请输入正确的数量")
        exit()
    dumper(xhr, number)


def interface(number, new_topic_id="", search_content=""):
    global results, image_count, thumbnails, topic_id
    if new_topic_id:
        topic_id = new_topic_id
    results = []
    thumbnails = []
    image_count = 0
    try:
        web = requests.get(basic_api_url + topic_id)
        xhr = web.json()
        if search_content:
            search_service(xhr, number, search_content)
        else:
            dumper(xhr, number, thumbnail=True)
        download(results, return_name=True, no_ext_name=True)
        return [thumbnails, results, names_without_ext, names]
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        raise ConnectionError


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
