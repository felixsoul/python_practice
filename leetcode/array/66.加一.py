#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
import unittest


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits


# @lc code=end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_plusOne_GeneralCase(self):
        self.assertEqual(self.sol.plusOne([1, 2, 3]), [1, 2, 4])

    def test_plusOne_CarryCase(self):
        self.assertEqual(self.sol.plusOne([1, 9, 9]), [2, 0, 0])

    def test_plusOne_AllNines(self):
        self.assertEqual(self.sol.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_plusOne_SingleDigitNine(self):
        self.assertEqual(self.sol.plusOne([9]), [1, 0])

    def test_plusOne_SingleDigitLessThanNine(self):
        self.assertEqual(self.sol.plusOne([5]), [6])

    def test_plusOne_EmptyList(self):
        self.assertEqual(self.sol.plusOne([]), [1])

    def test_plusOne_SingleZero(self):
        self.assertEqual(self.sol.plusOne([0]), [1])


if __name__ == '__main__':
    unittest.main()
