x = float(input("请输入一个数值:"))
abs_x = x

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
    abs_x = -x
print("该数的绝对值是：", abs_x)