from selenium import webdriver
from global_variables import driver_path_mac
from time import sleep

browser = webdriver.Chrome(driver_path_mac)
browser.implicitly_wait(10)
browser.get('https://www.baidu.com')

search_windows = browser.current_window_handle

browser.find_element_by_link_text('登录').click()
browser.find_element_by_link_text('立即注册').click()

all_handles = browser.window_handles

for handle in all_handles:
    if handle !=search_windows:
        browser.switch_to.window(handle)
        print(browser.title)
        browser.find_element_by_name('userName').send_keys('username')
        browser.find_element_by_name('phone').send_keys('138xxxxxxxx')
        sleep(2)
        browser.close()

browser.switch_to_window(search_windows)
print(browser.title)