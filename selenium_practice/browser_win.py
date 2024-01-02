from selenium import webdriver
from global_variables import driver_path_office

browser = webdriver.Chrome(driver_path_office)
browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()