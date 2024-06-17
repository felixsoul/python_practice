list1 = [1,2,3,4]
list2 = list1
list3 = list1.copy()

list2[0]='a'
list2[1]='b'
list2[2]='c'
list2[3]='d'

print(list1)
print(list2)
print(list3)
