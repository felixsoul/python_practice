# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from global_variables import driver_path
print("中文")
options = Options()
options.add_argument('--lang=zh-CN')
browser = webdriver.Chrome(driver_path,chrome_options=options)
browser.get("https://www.baidu.com")

above = browser.find_element_by_id('s-usersetting-top')
ActionChains(browser).move_to_element(above).perform()