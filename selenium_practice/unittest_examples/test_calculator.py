import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
     
    def test_div(self):
        c = Calculator(5, 0)
        result = c.div()
        self.assertEqual(result, 9)

    def test_add(self):
        c = Calculator(3,5)
        result = c.add()
        self.assertEqual(result, 8)
    
    def test_sub(self):
        c = Calculator(7,2)
        result = c.sub()
        self.assertEqual(result, 5)
    
    def test_mul(self):
        c = Calculator(3,3)
        result = c.mul()
        self.assertEqual(result, 9)
    
   

if __name__ == '__main__':
    unittest.main()