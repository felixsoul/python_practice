my_list = [1,1.0,'12ab', True, [1, 1.0, '1'], {1}, {1:1.0}]

print(my_list)

my_list[2] = '123'
print(my_list)

my_list.insert(2, 'inserted')
print(my_list)

my_list.append('tail')
print(my_list)

del my_list[-1]
print(my_list)

my_list.remove('123')
print(my_list)

if '123' in my_list:
    print('Yest')
else:
    print('No')

my_list.reverse()
print(my_list)

letters = ['J', 'a', 'm', 'e', 's']
word = '_'.join(letters)
print(word)

