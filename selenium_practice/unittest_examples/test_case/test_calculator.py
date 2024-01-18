import unittest
from calculator import Calculator

class TestAdd(unittest.TestCase):
    """add()方法测试"""
    def test_add_integer(self):
        """整数相加测试"""
        c = Calculator(3,5)
        self.assertEqual(c.add(), 8)
    
    def test_add_decimals(self):
        """小数相加测试"""
        c = Calculator(3.2, 5.5)
        self.assertEqual(c.add(),8)
    
class TestSub(unittest.TestCase):
    def test_sub_inter(self):
        c = Calculator(9, 2)
        self.assertEqual(c.sub(), 7)

    def test_sub_decimals(self):
        c = Calculator(8.8, 2.1)
        self.assertEqual(c.sub(),7)


if __name__ == '__main__':
    unittest.main()
    