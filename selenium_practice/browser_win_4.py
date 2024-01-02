from selenium import webdriver
from global_variables import driver_path_office
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(driver_path_office)
browser.get('https://www.baidu.com')
element = WebDriverWait(browser,5,0.5).until(
    EC.visibility_of_element_located((By.ID, "kw"))
)
element.send_keys("selenium")
#browser.quit()