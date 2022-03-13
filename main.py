#!/usr/bin/python3
import os
import re
import sys
from wget import downloadProvider
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Utilities:
    def __init__(self, driver):
        self.options = driver   # 加载对应浏览器驱动
        #if len(sys.argv) != 1:  # 当检测到传入数字时，不显示浏览器窗口(无头模式)
            # self.options.add_argument("--headless")
            # self.options.add_argument("--disable-gpu")

    def web_options(self):
        return self.options # 将最终的浏览器选项返回

    def loader(self, driver):   # 命令行版程序自由模式，可爬取网页上已加载的图片
        while len(sys.argv) == 1:
            userInput = str(input("更多？"))
            if userInput == ("y" or "Y"):
                driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')   # 向下滚动页面
            else:
                break

    def urlDumper(self, beautifulsoup_response):
        rule = re.compile(r'[(](.*?)[)]', re.S)  # 筛选规则，提取括号内URL
        rawImageList = re.findall(rule, str(beautifulsoup_response))
        converedURL = []
        for raw in rawImageList:
            process1 = raw.replace('"', "")  # 从两侧引号中提取url
            process2 = process1.find("@")
            process1 = process1[:process2]   # process2用于加载原始图片地址
            finalURL = process1.replace("//", "https://")   # 补全url
            converedURL.append(finalURL)
        return converedURL

    def _filter(self, response, keyword_1="", keyword_2="", reverse=False):
        # 提取器
        skipper = len(keyword_1)
        response = str(response)
        if reverse:
            # 反向查找并提取
            filterLeft = response.rfind(keyword_1)
            if keyword_2 != "":
                filterRight = response.find(keyword_2)
            else:
                filterRight = None
        else:
            filterLeft = response.find(keyword_1) + skipper + 1
            filterRight = response.rfind(keyword_2)
        return response[filterLeft:filterRight]

    def runtime(self, lists):
        convertedList = []
        for item in lists:
            information = {"user_name": self._filter(item.find_all("div", {"class": "user-name"}), '"_blank"', "</a>"),
                           "image_url": self.urlDumper(item.find_all("div", {"class": "img-content"})),
                           "post_time": self._filter(item.find_all("div", {"class": "time"}), '"_blank"', "</a>")}
            convertedList.append(information)
        return convertedList


def start(browser, number=0):
    # 程序的起点。默认要求的数量为0
    number = int(number)
    if number > 0:
        sys.argv.append(number)

    try:
        # 浏览器的选择
        if browser == "Microsoft Edge":
            from selenium.webdriver.edge.options import Options
            webdriver_option = Utilities(Options()).web_options()
            driver = webdriver.Edge(options=webdriver_option)
        if browser == "Google Chrome":
            from selenium.webdriver.chrome.options import Options
            webdriver_option = Utilities(Options()).web_options()
            driver = webdriver.Chrome(options=webdriver_option)
        if browser == "Apple Safari":
            from selenium.webdriver.safari.options import Options
            webdriver_option = Utilities(Options()).web_options()
            driver = webdriver.Edge(options=webdriver_option)
    except:
        sys.exit(1)
    URL = "https://t.bilibili.com/topic/8807683/"  # fursuitfriday页面URL
    driver.get(URL)

    try:
        # 等待网页加载
        WebDriverWait(driver, timeout=10, poll_frequency=0.5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "img-content")))
    except EC.NoSuchElementException:
        print("未能找到任何的图片。程序退出。")
        exit(1)

    Utilities(Options()).loader(driver)

    webpage = driver.page_source  # 获取网页源代码

    soup = BeautifulSoup(webpage, "lxml")

    lists = soup.find_all("div", {'class': 'main-content'})  # 查找动态内容
    response = Utilities(Options()).runtime(lists)  # 处理完毕的数据

    ending = False

    if len(sys.argv) != 1:
        required_number = int(sys.argv[1])
        if required_number < len(lists):
            response = response[:required_number]
        while len(lists) < required_number:
            driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')
            webpage = driver.page_source  # 获取网页源代码
            soup = BeautifulSoup(webpage, "lxml")
            lists = soup.find_all("div", {'class': 'main-content'})  # 同上
            response = Utilities(Options()).runtime(lists)  # 同上
            if len(soup.find_all("p", {"class": "end-text"})):
                ending = True
                break
            if len(response) >= required_number:
                response = response[:required_number]

    driver.quit()  # 关闭浏览器 节省资源

    if response:
        # 遍历返回的数据，写入文件
        with open("URLs.txt", "a+") as file:
            for combined_item in response:
                for item in combined_item["image_url"]:
                    file.write(item + "\n")
        # 当gui输入了数字，不调用wget.py
        if number > 0:
            downloadProvider(False)
        else:
            downloadProvider()
    else:
        # 检测到列表为空时不启用下载器
        downloadProvider(False)

    # 返回信息给gui
    return response, ending


if os.path.exists("URLs.txt"):  # 删除已经存在的urls
    os.remove("URLs.txt")

if __name__ == "__main__":
    start("Microsoft Edge")  # 默认为edge
