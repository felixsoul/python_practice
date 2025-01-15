#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answers = []
        L = [1]
        R = [1]
        nums_len = len(nums)
        for i in range(1, nums_len):
            L.append(nums[i-1]*L[i-1])
            R.append(nums[nums_len-i]*R[i-1])
        for i in range(nums_len):
            answers.append(L[i]*R[i])

        return R, answers


test = Solution()
print(test.productExceptSelf([1, 2, 3, 4, 5]))
# @lc code=end
