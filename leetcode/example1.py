def algorithm(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []
