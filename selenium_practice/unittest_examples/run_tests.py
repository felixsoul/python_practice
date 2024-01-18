import unittest

test_dir = './test_case'
suite = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    runnner = unittest.TextTestRunner()
    runnner.run(suite)