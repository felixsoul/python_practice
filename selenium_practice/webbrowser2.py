from selenium import webdriver
from global_variables import *

browser = webdriver.Chrome(driver_path)
browser.get("https://www.baidu.com")
'''
browser.find_element_by_id("kw").clear()
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
browser.quit()
'''

#browser.get("https://www.baidu.com")
search_text = browser.find_element_by_id("kw")
search_text.send_keys("selenium")
search_text.submit()