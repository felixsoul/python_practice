import copy

a = [1, 2, 3]
b = a 
c = [1, 2, 3]
d = a.copy()

print(a is b)
print(a is not c)
print(a == c)
print(a == d)
print(a is d)

a_2_layers = [1,2,[3,4]]
d_2_layers = a_2_layers.copy()
e_2_layers = copy.deepcopy(a_2_layers)

print(a_2_layers is d_2_layers)
print(a_2_layers[2] is d_2_layers[2])

print(a_2_layers is e_2_layers)
print(a_2_layers[2] is e_2_layers[2])