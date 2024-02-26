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
all_handles = browser.window_handles
sleep(2)
for handle in all_handles:
    print(handle)
    
browser.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()

sleep(2)
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)                   
alert.accept()
browser.quit()
