# import json #启用该行以调用cookie登录
import os
import re
from typing import Tuple
from bs4 import BeautifulSoup
from selenium import webdriver

if os.path.exists("URLs.txt"): #删除已经存在的urls
    os.remove("URLs.txt")

'''
    下面的是命令行模式（headless），取消注释可用
'''
# options = webdriver.ChromeOptions() 
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")

driver = webdriver.Chrome() #调用chrome，调用命令行在括号内加options=options
URL = "https://t.bilibili.com/topic/8807683/" #fursuitfriday页面URL
driver.get(URL)

'''
    网页cookie加载(备用)
'''
# with open('cookie.txt','r') as f:
#     cookieList = json.load(f)
#     for cookie in cookieList:
#         driver.add_cookie(cookie)
#driver.refresh()

driver.implicitly_wait(10)  #等待网页加载

while True:
    userInput = str(input("更多？"))
    if userInput == "y" or "Y":
        driver.execute_script('window.scrollBy(0,1000)')
    else:
        break

webpage = driver.page_source  #获取网页源代码

driver.quit() #关闭浏览器 节省资源

soup = BeautifulSoup(webpage, "lxml")
# print(soup.prettify())

# print(soup.prettify())

lists = soup.find_all("div", {'class':'img-content'}) #寻找带img-content类的div（含图片框）
rule = re.compile(r'[(](.*?)[)]', re.S) #筛选规则，提取括号内URL


for raw in lists:
    trans = str(raw)
    pickZero = re.findall(rule,trans)[0]
    process1 = pickZero.replace('"',"")
    process2 = process1.find("@")
    process1 = process1[:process2]
    finalURL = process1.replace("//","https://")
    
    with open("URLs.txt","a+") as buffer:   #写入文件
        buffer.write(finalURL+"\n")

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
