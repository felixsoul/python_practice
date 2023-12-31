from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from global_variables import *
browser = webdriver.Chrome(driver_path)
browser.get("https://www.baidu.com")

size = browser.find_element_by_id('kw').size
print(size)

elements= browser.find_elements_by_xpath('//div[@class="s-bottom-layer-content"]//p')
for element in elements:
    try:
        a_tag = element.find_element_by_xpath('./a')
        print(a_tag.get_attribute('textContent'))
        print(a_tag.get_attribute('href'))
    except NoSuchElementException:
        try:
            span_tag = element.find_element_by_xpath('./span')
            print(span_tag.get_attribute('textContent'))
        except NoSuchElementException:
            print("No tag a or span is found")

browser.quit()



"""
/html/body/div[2]/div[1]/div[7]/div/p[1]/a
//*[@id="bottom_layer"]/div/p[1]/a
//*[@id="bottom_layer"]/div/p[1]/a
"""