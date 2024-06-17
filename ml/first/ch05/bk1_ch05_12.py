list_0 = [0,1,2,3,4,5,6,7,8]

first, *list_rest = list_0
print(list_rest)

first, second, *list_rest = list_0
print(list_rest)

first, second, *list_rest, last = list_0
print(list_rest)

first, *list_rest, _ = list_0
print(list_rest)

list1 = [1,2,3,4,5]
list2 = [6,7,8]
combined_list = [*list1, *list2]
print(combined_list)
print([list1,list2])
list3 = list1 + list2
print(list3)

