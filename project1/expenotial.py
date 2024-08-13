def expential(n)->int:
    count = 0
    base = 1
    nums = []
    for _ in range(n):
        for _ in range(base):
            count += 1
            nums.append(count)
        base *= 2
    print(nums)
    return count


if __name__  == "__main__":
    print(expential(4))