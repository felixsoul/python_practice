def bubble_sort(nums: list[int])->int:
    count = 0
    for i in range(len(nums)-1, 0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                count += 3
    return count

nums = [5,4,3,2,1]
print(bubble_sort(nums))
print(nums)