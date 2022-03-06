# import json #启用该行以调用cookie登录
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import sys

if os.path.exists("URLs.txt"):  # 删除已经存在的urls
    os.remove("URLs.txt")

options = webdriver.ChromeOptions()
arg = len(sys.argv)


def urlDumper(beautifulsoup_response):
    rule = re.compile(r'[(](.*?)[)]', re.S)  # 筛选规则，提取括号内URL
    rawImageList = re.findall(rule, str(beautifulsoup_response))
    converedURL = []
    for raw in rawImageList:
        process1 = raw.replace('"', "")
        process2 = process1.find("@")
        process1 = process1[:process2]
        finalURL = process1.replace("//", "https://")
        converedURL.append(finalURL)

    return converedURL


if arg != 1:
    try:
        command = int(sys.argv[1])
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    except ValueError:
        arg = 1
        options = webdriver.ChromeOptions()
        print("wrong input")

driver = webdriver.Chrome(options=options)  # 调用chrome，调用命令行在括号内加options=options
URL = "https://t.bilibili.com/topic/8807683/"  # fursuitfriday页面URL
driver.get(URL)

'''
    网页cookie加载(备用)
'''
# with open('cookie.txt','r') as f:
#     cookieList = json.load(f)
#     for cookie in cookieList:
#         driver.add_cookie(cookie)
# driver.refresh()

driver.implicitly_wait(10)  # 等待网页加载

while arg == 1:
    userInput = str(input("更多？"))
    if userInput == ("y" or "Y"):
        driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')
    else:
        break

webpage = driver.page_source  # 获取网页源代码

soup = BeautifulSoup(webpage, "lxml")
# print(soup.prettify())

# print(soup.prettify())

lists = soup.find_all("div", {'class': 'img-content'})  # 寻找带img-content类的div（含图片框）
response = urlDumper(lists)  # 处理完毕的URL列表

if arg != 1:
    while len(response) < command:
        driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')
        driver.implicitly_wait(10)
        webpage = driver.page_source  # 获取网页源代码

        soup = BeautifulSoup(webpage, "lxml")
        # print(soup.prettify())

        # print(soup.prettify())

        lists = soup.find_all("div", {'class': 'img-content'})  # 寻找带img-content类的div（含图片框）
        response = urlDumper(lists)  # 处理完毕的URL列表
        response = response[:command]

driver.quit()  # 关闭浏览器 节省资源

with open("URLs.txt", "a+") as file:
    for item in response:
        file.write(item)

print("Done")

'''
    下面的代码是python语言自带的下载器，会经常抽风，未启用
'''
# print(downloadList)
# def downloader(downloadList):
#     number = 1
#     for file in downloadList:
#         response = requests.get(file)
#         filename = str(number) + str(file[-4:])
#         with open(filename,"wb") as code:
#             code.write(response.content)
#         print(number)
#         number += 1

# downloader(downloadList)
