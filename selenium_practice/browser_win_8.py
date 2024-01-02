from selenium import webdriver
from global_variables import driver_path_office
from time import sleep

browser = webdriver.Chrome(driver_path_office)
browser.get('https://www.126.com')
sleep(2)

login_frame = browser.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
browser.switch_to_frame(login_frame)
browser.find_element_by_name("email").send_keys("username")
browser.find_element_by_name("password").send_keys("password")
browser.find_element_by_id("dologin").click()
browser.switch_to_default_content()

browser.quit()