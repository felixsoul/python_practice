from selenium import webdriver
from global_variables import driver_path_office
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(driver_path_office)
browser.get("https://www.baidu.com")

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
browser.find_element_by_id("kw").send_keys("教程")
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
browser.find_element_by_id('su').send_keys(Keys.ENTER)
