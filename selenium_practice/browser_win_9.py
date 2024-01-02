from selenium import webdriver
from global_variables import driver_path_office
from selenium.webdriver import ActionChains

browser = webdriver.Chrome(driver_path_office)
browser.get('https://www.baidu.com')

above = browser.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(browser).move_to_element(above).perform()
option_to_select = browser.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()