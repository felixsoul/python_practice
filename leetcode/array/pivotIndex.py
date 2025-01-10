def pivotIndex(nums):
    left_sum = 0
    right_sum = sum(nums)
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1


# Test
print(pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
print(pivotIndex([1, 2, 3]))  # -1
print(pivotIndex([2, 1, -1]))  # 0
print(pivotIndex([1, 2, 3, 4, 6, 6, 5, 4, 3, 2, 1]))  # -1
print(pivotIndex([1, 2, 3, 4, 6, 6, 5, 4, 3, 2, 1, 0]))  # 10

for i in range(5):
    print(i)
