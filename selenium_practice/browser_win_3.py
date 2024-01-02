from time import sleep
from selenium import webdriver
from global_variables import driver_path_office
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(driver_path_office)
browser.get("https://www.baidu.com")
title = browser.title
print("title: %s" %title)

now_url = browser.current_url
print("URL: %s" %now_url)


browser.find_element_by_id('kw').send_keys("selenium")
browser.find_element_by_id('kw').send_keys(Keys.ENTER)

sleep(3)
print("=============After search========")
title = browser.title
print("title: %s" %title)

now_url = browser.current_url
print("URL: %s" %now_url)

#find_element_by_css_selector('.class1.class2')
num = browser.find_element_by_css_selector('.hint_PIwZX.c_font_2AD7M').text
#num = browser.find_element_by_class_name("hint_PIwZX").text
print("result: %s" %num)


