name = 'James'
height = 181.18
str_1 = name + ' has a height of '+ str(height)+' cm.'
print(str_1)

str2 = '%s has a height of %.3f cm.' %(name, height)
print(str2)

str3 = '{} has a height of {:.3f} cm.'.format(name, height)
print(str3)

str4 = f'{name} has a height of {height:.3f} cm.'
print(str4)

