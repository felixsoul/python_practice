import unittest


class Solution:
    def SelectionSort(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            mix_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[mix_index]:
                    mix_index = j
            if mix_index != i:
                nums[i], nums[mix_index] = nums[mix_index], nums[i]
        return nums


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_SelectionSort_EmptyList_ReturnsEmptyList(self):
        self.assertEqual(self.sol.SelectionSort([]), [])

    def test_SelectionSort_SingleElementList_ReturnsSameList(self):
        self.assertEqual(self.sol.SelectionSort([1]), [1])

    def test_SelectionSort_AlreadySorted_ReturnsSameList(self):
        self.assertEqual(self.sol.SelectionSort(
            [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_SelectionSort_ReverseOrder_ReturnsSorted(self):
        self.assertEqual(self.sol.SelectionSort(
            [5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_SelectionSort_WithDuplicates_ReturnsSorted(self):
        self.assertEqual(self.sol.SelectionSort(
            [3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_SelectionSort_RandomOrder_ReturnsSorted(self):
        self.assertEqual(self.sol.SelectionSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [
                         1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
