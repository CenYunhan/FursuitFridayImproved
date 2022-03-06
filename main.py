# import json #启用该行以调用cookie登录
import os
import re
import sys
from wget import downloadProvider
from bs4 import BeautifulSoup
from selenium import webdriver

if os.path.exists("URLs.txt"):  # 删除已经存在的urls
    os.remove("URLs.txt")
if not os.path.exists("images"):
    os.mkdir("images")

options = webdriver.ChromeOptions()
arg = len(sys.argv)


def fileProvider(finalURL, folder):
    index = finalURL.rfind("/") + 1
    fileName = finalURL[index:]
    if fileName not in folder:
        return finalURL
    else:
        pass


def urlDumper(beautifulsoup_response, folder, mode):
    rule = re.compile(r'[(](.*?)[)]', re.S)  # 筛选规则，提取括号内URL
    rawImageList = re.findall(rule, str(beautifulsoup_response))
    converedURL = []
    for raw in rawImageList:
        process1 = raw.replace('"', "")
        process2 = process1.find("@")
        process1 = process1[:process2]
        finalURL = process1.replace("//", "https://")
        if mode == "Differ":
            callback = fileProvider(finalURL, folder)
            if callback is not None:
                converedURL.append(callback)
        if mode == "Full":
            converedURL.append(finalURL)
    return converedURL


userMode = "Differ"

if arg != 1:
    try:
        command = int(sys.argv[1])
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    except ValueError:
        arg = 1
        options = webdriver.ChromeOptions()
        print("wrong input")

    try:
        userMode = str(sys.argv[2])
    except IndexError or ValueError:
        pass
if userMode == "Full":
    print("Full mode detected")
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

folder = os.listdir("images")
lists = soup.find_all("div", {'class': 'img-content'})  # 寻找带img-content类的div（含图片框）
response = urlDumper(lists, folder, "Full")  # 处理完毕的URL列表

if arg != 1:
    while len(lists) < command:
        downloadedNumber = len(folder)
        dumpedNumber = len(lists)
        driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')
        webpage = driver.page_source  # 获取网页源代码
        soup = BeautifulSoup(webpage, "lxml")
        lists = soup.find_all("div", {'class': 'img-content'})  # 寻找带img-content类的div（含图片框）
        response = urlDumper(lists, folder, userMode)  # 处理完毕的URL列表
        if len(response) >= dumpedNumber:
            response = response[:command]
        else:
            response = response[:(command - downloadedNumber - 1)]

driver.quit()  # 关闭浏览器 节省资源

if response:
    with open("URLs.txt", "a+") as file:
        for item in response:
            file.write(item + "\n")
    downloadProvider()
else:
    downloadProvider(False)

print("Done")
