from selenium import webdriver
driver_path = "/Users/hunter/local/chromedriver-mac-x64/chromedriver"
#driver_path = "/Users/hunter/local/chromedriver-mac-x64/chromedriver"
#driver = webdriver.Chrome(driver_path)
driver_path = "D:\\local\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
#driver.quit()