from selenium import webdriver
from global_variables import driver_path_office
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome(driver_path_office)
browser.get('https://www.baidu.com')
browser.find_element_by_id('kw').send_keys("selenium")
browser.find_element_by_id('kw').send_keys(Keys.ENTER)
sleep(2)

texts = browser.find_elements_by_xpath("//div[@tpl = 'se_com_default']/div/div/h3/a")
print(len(texts))
for t in texts:
    print(t.text)