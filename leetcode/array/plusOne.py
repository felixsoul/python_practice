def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # 如果当前数字为9，则将其置为0，继续向前遍历。
    # 当遍历完数组后，如果数组的第一个数字还是0，则需要在数组最前面插入一个1。
    digits.insert(0, 1)
    return digits


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9, 9, 9]))
"""
解题思路：
1. 从后往前遍历数组，如果当前数字小于9，则加1并返回数组。
2. 如果当前数字等于9，则将其置为0，继续向前遍历。
3. 如果遍历完数组后，数组的第一个数字还是0，则需要在数组最前面插入一个1。
"""
