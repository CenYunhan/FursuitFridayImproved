# import json #启用该行以调用cookie登录
import os
import re
import sys
from wget import downloadProvider
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Utilities():
    def __init__(self):
        self.options = Options()
        self.arg = len(sys.argv)
        if self.arg != 1:
            try:
                self.options.add_argument("--headless")
                self.options.add_argument("--disable-gpu")
            except ValueError:
                self.arg = 1
                self.options = Options()
                print("wrong input")

    def web_options(self):
        return self.options

    def argvs(self):
        return self.arg

    def loader(self):
        while self.arg == 1:
            userInput = str(input("更多？"))
            if userInput == ("y" or "Y"):
                driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')
            else:
                break

    def fileProvider(self, finalURL, folder):
        index = finalURL.rfind("/") + 1
        fileName = finalURL[index:]
        if fileName not in folder:
            return finalURL
        else:
            pass

    def urlDumper(self, beautifulsoup_response, folder=[]):
        rule = re.compile(r'[(](.*?)[)]', re.S)  # 筛选规则，提取括号内URL
        rawImageList = re.findall(rule, str(beautifulsoup_response))
        converedURL = []
        for raw in rawImageList:
            process1 = raw.replace('"', "")
            process2 = process1.find("@")
            process1 = process1[:process2]
            finalURL = process1.replace("//", "https://")
            if folder:
                callback = self.fileProvider(finalURL, folder)
                if callback is not None:
                    converedURL.append(callback)
            else:
                converedURL.append(finalURL)
        return converedURL

def start():
    driver = webdriver.Edge(r"C:\Users\admin\PycharmProjects\FurGUI\venv\Scripts\msedgedriver.exe",
                            options=Utilities().web_options())  # 调用chrome，调用命令行在括号内加options=options
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

    try:
        WebDriverWait(driver, timeout=10, poll_frequency=0.5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "img-content")))
        # 等待网页加载
    except EC.NoSuchElementException:
        print("No such element")

    webpage = driver.page_source  # 获取网页源代码

    soup = BeautifulSoup(webpage, "lxml")

    folder = os.listdir("images")
    print(soup.prettify())
    lists = soup.find_all("div", {'class': 'img-content'})  # 寻找带img-content类的div（含图片框）
    response = Utilities().urlDumper(lists, folder)  # 处理完毕的URL列表

    if Utilities().argvs() != 1:
        while len(lists) < Utilities.command:
            downloadedNumber = len(folder)
            dumpedNumber = len(lists)
            driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')
            webpage = driver.page_source  # 获取网页源代码
            soup = BeautifulSoup(webpage, "lxml")
            lists = soup.find_all("div", {'class': 'img-content'})  # 寻找带img-content类的div（含图片框）
            response = Utilities().urlDumper(lists, folder)  # 处理完毕的URL列表
            if len(response) >= dumpedNumber:
                response = response[:Utilities.command]
            else:
                response = response[:(Utilities.command - downloadedNumber - 1)]

    driver.quit()  # 关闭浏览器 节省资源

    if response:
        with open("URLs.txt", "a+") as file:
            for item in response:
                file.write(item + "\n")
        downloadProvider()
    else:
        downloadProvider(False)

    print("Done")


if os.path.exists("URLs.txt"):  # 删除已经存在的urls
    os.remove("URLs.txt")
if not os.path.exists("images"):
    os.mkdir("images")

if __name__ == "__main__":
    start()

