# -*- coding: utf-8 -*- 
from selenium import webdriver
from global_variables import driver_path_office
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
browser = webdriver.Chrome(driver_path_office)
browser.get("https://www.baidu.com")
main_window = browser.current_window_handle
print(main_window)
above = browser.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(browser).move_to_element(above).perform()
option_to_select = browser.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()

sleep(5)
browser.find_element_by_css_selector('li.item.cur[data-tabid="advanced"][href="#advanced"]').click()
#browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()