class Solution:
    def insertionSort(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            tmp = nums[i]
            j = i
            while j > 0 and nums[j-1] > tmp:
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = tmp
        return nums


if __name__ == '__main__':
    test = Solution()
    print(test.insertionSort([5, 6, 8, 1, 2, 3, 4]))
