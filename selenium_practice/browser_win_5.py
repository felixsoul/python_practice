from time import sleep,ctime
from selenium import webdriver
from global_variables import driver_path_office

browser = webdriver.Chrome(driver_path_office)
browser.get('https://www.baidu.com')

print(ctime())

for i in range(10):
    try:
        el = browser.find_element_by_id('kw22')
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
print(ctime())
browser.quit()