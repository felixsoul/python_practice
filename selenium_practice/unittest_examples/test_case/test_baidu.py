import unittest
from selenium import webdriver
from time import sleep
from global_variables import driver_path_office

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(driver_path_office)
        cls.base_url = "https://www.baidu.com"
    
    def test_search_key_selenium(self):
        self.browser.get(self.base_url)
        self.browser.find_element_by_id("kw").send_keys("selenium")
        self.browser.find_element_by_id("su").click()
        sleep(2)
        title = self.browser.title
        self.assertEqual(title, "selenium_百度搜索")

    def test_search_key_unittest(self):
        self.browser.get(self.base_url)
        self.browser.find_element_by_id("kw").send_keys("unittest")
        self.browser.find_element_by_id("su").click()
        sleep(2)
        title = self.browser.title
        self.assertEqual(title, "unittest_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
    

if __name__ == "__main__":
    unittest.main()