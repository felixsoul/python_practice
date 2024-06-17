my_list = [1,1.0,'1', True, [1, 1.0, '1'], {1}, {1:1.0}]
print(f'列表长度:{len(my_list)}')

for index, item in enumerate(my_list):
    type_i = type(item)
    print(f"元素:{item}, 索引:{index}, 类型:{type_i}")

print(my_list[0])
print(my_list[1])

print(my_list[-1])
print(my_list[-2])

print(my_list[:3])
print(my_list[1:4])

print(my_list[::2])

print(my_list[::-1])

print(my_list[4][1])