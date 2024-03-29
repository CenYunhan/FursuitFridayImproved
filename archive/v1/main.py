#!/usr/bin/python3
import os
import re
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def web_options(driver_options):
    options = driver_options  # 加载对应浏览器驱动
    if len(sys.argv) != 1:  # 当检测到传入数字时，不显示浏览器窗口(无头模式)
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    return options  # 将最终的浏览器选项返回


def urlDumper(beautifulsoup_response):
    rule = re.compile(r'[(](.*?)[)]', re.S)  # 筛选规则，提取括号内URL
    rawImageList = re.findall(rule, str(beautifulsoup_response))
    converedURL = []
    for raw in rawImageList:
        process1 = raw.replace('"', "")  # 从两侧引号中提取url
        process2 = process1.find("@")
        process1 = process1[:process2]  # process2用于加载原始图片地址
        finalURL = process1.replace("//", "https://")  # 补全url
        converedURL.append(finalURL)
    return converedURL


def _filter(response, keyword_1="", keyword_2="", reverse=False):
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


def runtime(lists):
    convertedList = []
    for item in lists:
        information = {"user_name": _filter(item.find_all("div", {"class": "user-name"}), '"_blank"', "</a>"),
                       "image_url": urlDumper(item.find_all("div", {"class": "img-content"})),
                       "post_time": _filter(item.find_all("div", {"class": "time"}), '"_blank"', "</a>")}
        convertedList.append(information)
    return convertedList


defaultURL = "https://t.bilibili.com/topic/8807683/"  # fursuitfriday页面URL


def start(browser, number=0, URL=defaultURL):
    # 程序的起点。默认要求的数量为0
    number = int(number)
    if number > 0:
        sys.argv.append(number)

        # 浏览器的选择
    if browser == "Microsoft Edge":
        from selenium.webdriver.edge.options import Options
        webdriver_option = web_options(Options())
        driver = webdriver.Edge(options=webdriver_option)
    if browser == "Google Chrome":
        from selenium.webdriver.chrome.options import Options
        webdriver_option = web_options(Options())
        driver = webdriver.Chrome(options=webdriver_option)
    if browser == "Mozilla Firefox":
        from selenium.webdriver.firefox.options import Options
        webdriver_option = web_options(Options())
        driver = webdriver.Firefox(options=webdriver_option)
    driver.get(URL)

    try:
        # 等待网页加载
        WebDriverWait(driver, timeout=10, poll_frequency=0.5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "img-content")))
    except EC.NoSuchElementException:
        print("未能找到任何的图片。程序退出。")
        exit(1)

    if len(sys.argv) == 1:
        userInput = input("进入自由模式。等待用户……(按任意键和回车继续)  ")
        while userInput:
            break

    webpage = driver.page_source  # 获取网页源代码

    soup = BeautifulSoup(webpage, "lxml")

    lists = soup.find_all("div", {'class': 'main-content'})  # 查找动态内容
    response = runtime(lists)  # 处理完毕的数据

    ending = False

    if len(sys.argv) > 1:
        required_number: int  # 意图
        required_number = int(sys.argv[1])
        if required_number < len(lists):
            response = response[:required_number]
        while len(lists) < required_number:
            driver.execute_script('window.scrollTo(0,window.document.body.scrollHeight)')
            webpage = driver.page_source  # 获取网页源代码
            soup = BeautifulSoup(webpage, "lxml")
            lists = soup.find_all("div", {'class': 'main-content'})  # 同上
            response = runtime(lists)  # 同上
            if len(soup.find_all("p", {"class": "end-text"})):
                ending = True
                break
            if len(response) >= required_number:
                response = response[:required_number]

    driver.quit()  # 关闭浏览器 节省资源

    if response:
        with open("URLs.txt", "a+") as file:
            for combined_item in response:
                for item in combined_item["image_url"]:
                    file.write(item + "\n")

    # 返回信息给gui
    return response, ending


if os.path.exists("URLs.txt"):  # 删除已经存在的urls
    os.remove("URLs.txt")

if __name__ == "__main__":
    start("Microsoft Edge")  # 默认为edge
