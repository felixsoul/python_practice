#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 轮转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


# @lc code=end
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(nums[-k:])
print(nums[-1:])
print(nums[-2:])
print(nums[-3:])
print(nums[:-k])
print(nums[:-1])
print(nums[:-2])
