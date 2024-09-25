import random

def random_numbers(n:int)->list[int]:
    nums = [i for i in range(1, n+1)]
    random.shuffle(nums)
    return nums

def find_one(nums: list[int])->int:
    for i in range(len(nums)):
        if nums[i]== 1:
            return i
    else:
        return -1

if __name__ == '__main__':
    n = 1000
    nums = random_numbers(n)
    print(find_one(nums))