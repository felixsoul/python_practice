def rotate(nums, k):
    if k > len(nums):
        k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))
    a = [1, 2, 3, 4, 5, 6, 7]
    print(a[-3:])
    print(a[:-3])
    print(a[-1])