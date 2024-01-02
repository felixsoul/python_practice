from time import ctime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from global_variables import driver_path_office

browser = webdriver.Chrome(driver_path_office)
browser.get('https://www.baidu.com')
browser.implicitly_wait(10)
try:
    print(ctime())
    browser.find_element_by_id('kw22').send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    browser.quit()