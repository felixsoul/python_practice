import unittest
import htmltestreport
from test_case.test_baidu import TestBaidu
test_dir = './test_case'
suite = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    fp = open('./test_report/result.html','wb')
    # runnner = unittest.TextTestRunner()
    # runnner.run(suite)
    suite = unittest.TestSuite()
    suite.addTest(TestBaidu("test_search_key_selenium"))
    runner = htmltestreport.HTMLTestReport('./test_report/result.html',title="Test Baidu", description="测试百度" )
    #runner = htmltestreport.HTMLTestReport(fp,title="Test Baidu", description="测试百度")
    runner.run(suite)