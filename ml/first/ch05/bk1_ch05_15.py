import copy

list1 = [1,2,3,[4,5]]
print(f"The origin list:{list1}")

list_deep = copy.deepcopy(list1)

list2 = list1.copy()
list3 = list1[:]
list4 = list(list1)
list5 = [*list1]

list_deep[3][0]= ['deep']
list_deep[2] = 'worked_0'

list2[3][0] = 'abc'
list2[2] = 'worked_1'

list3[3][0]='X1'
list3[2] = 'worked_2'

list4[3][0]= 'X2'
list4[2]='worked_3'

list5[3][0]='X3'
list5[2]='worked_4'

print(list1)
print(list_deep)

print(list2)
print(list3)
print(list4)
print(list5)