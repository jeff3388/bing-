from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import requests
import time
import re

path = 'geckodriver.exe'
driver = webdriver.Firefox(executable_path = path)
link = 'https://www.bing.com/'
driver.get(link)
driver.find_element_by_name("q").send_keys("python 教學")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

for w in range(8):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    li = soup.find_all("li", attrs={"class": "b_ad"})
    b = soup.find_all("li", attrs={"class": "b_algo"})

    word = str(soup).find('https://python-learnnotebook.blogspot.com')
    # 判斷是否在當頁面
    if word != -1:
        break
        
    else:
        driver.execute_script("window.scrollTo(0, 2500)")
        time.sleep(10)
        driver.find_element_by_css_selector(".sb_pagN").click() # 下一頁
        time.sleep(2)
        
# 如果跑完4頁都沒找到則關閉瀏覽器
if w != 7: 
    # 判斷是否有廣告欄位
    l = [l.find("a").get("href") for l in li]

    if len(l) != 0:
        c = 0
        for i in b:
            c += 1
            i = i.find("a").get("href")
            i = i.find("https://python-learnnotebook.blogspot.com")
            if i == 0:
                driver.find_element_by_css_selector("#b_results > li:nth-child(" + str(c+1) + ") > h2 > a").click()
    else:
        c = 0
        for i in b:
            c += 1
            i = i.find("a").get("href")
            i = i.find("https://python-learnnotebook.blogspot.com")
            if i == 0:
                driver.find_element_by_css_selector("#b_results > li:nth-child(" + str(c) + ") > h2 > a").click()
                