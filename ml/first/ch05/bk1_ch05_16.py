person = {'name':'James', 'age':88, 'gender':'male'}

fruits = dict(apple=88, banana=888, cherry=8888)

print(person['name'])
print(fruits['cherry'])

person['age'] = 28
print(person)

person['city'] = 'Toronto'
print(person)

del person['gender']
print(person)

print(person.keys())
print(person.values())
print(person.items())

