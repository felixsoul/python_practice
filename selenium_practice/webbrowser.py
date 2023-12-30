from selenium import webdriver
driver_path = "/Users/hunter/local/chromedriver-mac-x64/chromedriver"
driver = webdriver.Chrome(driver_path)
first_url = "https://www.baidu.com"
print("now access %s" %(first_url))
driver.get(first_url)

second_url = 'https://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

print("back to %s" %(first_url))
driver.back()

print("forward to %s" %(second_url))
driver.forward()

driver.refresh()