from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from global_variables import driver_path_office
for i in range(10):
    browser = webdriver.Chrome(driver_path_office)
    browser.get("https://glpitest.ergo-china.cn/")
    title = browser.title
    print(title)
    sleep(3)
    browser.find_element_by_xpath('//*[@id="form-ad"]/button').send_keys(Keys.ENTER)
    sleep(3)
    print(browser.title)
    browser.find_element_by_xpath('/html/body/div[2]/header/div/div[2]/div/div[1]/div/a').send_keys(Keys.ENTER)
    browser.find_element_by_xpath('/html/body/div[2]/header/div/div[2]/div/div[1]/div/div/a[4]').send_keys(Keys.ENTER)
    browser.close()

