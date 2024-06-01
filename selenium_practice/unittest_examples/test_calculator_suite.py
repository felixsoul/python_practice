import unittest
from calculator import Calculator

class TestCalculatorSuite(unittest.TestCase):
    def setUp(self):
        print("test start:")
    
    def tearDown(self) -> None:
        print("test end")

    def test_add(self):
        print("test_add")
        c = Calculator(5,7)
        result = c.add()
        self.assertEqual(result, 12)

    def test_sub(self):
        print("test_sub")
        c = Calculator(8, 5)
        result = c.sub()
        self.assertEqual(result, 2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCalculatorSuite("test_add"))
    suite.addTest(TestCalculatorSuite("test_sub"))
    runner = unittest.TextTestRunner()
    runner.run(suite)