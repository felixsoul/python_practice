class Solution:
    def shellSort(self, nums: list[int]) -> list[int]:
        size = len(nums)
        gap = size // 2

        while gap > 0:
            for i in range(gap, size):
                j = i
                tmp = nums[i]
                while j > gap and 1:
                    pass


if __name__ == '__main__':
    test = Solution()
    test.shellSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
