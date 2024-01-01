from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from global_variables import driver_path

browser = webdriver.Chrome(driver_path)
browser.get('https://www.baidu.com')

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("kw")