def value(nums, index):
    if index < 0 or index >= len(nums):
        return -1
    return nums[index]


print(value([1, 2, 3, 4, 5], 3))  # 4


def find(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


print(find([1, 2, 3, 4, 5], 3))  # 2

arr = [1, 2, 3, 4, 5]
val = 6
arr.append(val)
print(arr)  # [1, 2, 3, 4, 5, 6]

arr = [1, 2, 3, 4, 5]
i, val = 2, 6
arr.insert(i, val)
print(arr)  # [1, 2, 6, 3, 4, 5]


def change(nums, index, val):
    if index < 0 or index >= len(nums):
        return
    nums[index] = val


change([1, 2, 3, 4, 5], 2, 6)
print(arr)  # [1, 2, 6, 4, 5]

arr = [1, 2, 3, 4, 5]
arr.pop()
print(arr)  # [1, 2, 3, 4]

arr = [1, 2, 3, 4, 5]
arr.pop(2)
print(arr)  # [1, 2, 4, 5]

arr = [1, 2, 3, 4, 5]
arr.pop()
print(arr)
# [1, 2, 3, 4]

arr = [1, 2, 3, 4, 5]
arr.pop(3)
print(arr)  # [1, 2, 3, 5]
# [1, 2, 3, 5]

arr = [1, 2, 3, 7, 5]
arr.remove(7)
print(arr)  # [1, 2, 4, 5]
print(arr[-1])
