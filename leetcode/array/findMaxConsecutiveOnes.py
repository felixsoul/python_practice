def findMaxConsecutiveOnes(nums):
    numbers = 0
    old_numbers = 0

    for i in range(len(nums)):
        print(i)
        if nums[i] == 1:
            numbers = numbers + 1
        else:
            if numbers > old_numbers:
                old_numbers = numbers
                numbers = 0
    return old_numbers


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
