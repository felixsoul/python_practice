import unittest


class Solution:
    def bubbleSort(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            flag = False
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
            if not flag:
                break
        return nums


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_BubbleSort_EmptyList_ReturnsEmptyList(self):
        self.assertEqual(self.sol.bubbleSort([]), [])

    def test_BubbleSort_SingleElementList_ReturnsSameList(self):
        self.assertEqual(self.sol.bubbleSort([1]), [1])

    def test_BubbleSort_AlreadySorted_ReturnsSameList(self):
        self.assertEqual(self.sol.bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_BubbleSort_ReverseOrder_SortsCorrectly(self):
        self.assertEqual(self.sol.bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_BubbleSort_RandomOrder_SortsCorrectly(self):
        self.assertEqual(self.sol.bubbleSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [
                         1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_BubbleSort_WithDuplicates_SortsCorrectly(self):
        self.assertEqual(self.sol.bubbleSort(
            [3, 3, 2, 2, 1, 1]), [1, 1, 2, 2, 3, 3])


if __name__ == '__main__':
    unittest.main()
