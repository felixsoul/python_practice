from selenium import webdriver
from global_variables import driver_path_office
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome(driver_path_office)
browser.get("https://www.baidu.com")

above = browser.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(browser).move_to_element(above).perform()
option_to_select = browser.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
all_handles = browser.window_handles

browser.find_element_by_class_name('prefpanelgo').click()

alert = browser.switch_to_alert

alert_text = alert.text
print(alert_text)

alert.accept()
browser.quit()