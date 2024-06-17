str = 'Hey, James!'
print(f'str字符串的长度为:{len(str)}')
for index, char in enumerate(str):
    print(f'索引:{index}, 字符:{char}')

print(f"字符串的索引1为:{str[1]}")
print(f"字符串的索引-1为:{str[-1]}")
print(f"字符串的索引-2为:{str[-2]}")
print(f"字符串str[:3]为:{str[:3]}")
print(f"字符串str[1:6]为:{str[1:6]}")
print(f"字符串str[::2]为:{str[::2]}")
print(f"字符串str[::-1la]为:{str[::-1]}")
