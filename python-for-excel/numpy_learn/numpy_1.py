import numpy as np

array1 = np.array([10, 100, 1000.])
print(array1.dtype)

array2 = np.array([[1., 2., 3.],
                  [4., 5., 6.]])


# print(array1+1)

# print(array2*array2)

# print(array2*array1)
# print(array1*array2)

# print(array2.T)

# print(array2.sum(axis=0))
# print(array2.sum(axis=1))

print(array1[2])

print(array2[0, 0])

print(array2[:, 1:])
print(array2[1, :2])

print(np.arange(2, 12).reshape(1, 10))

array3 = np.arange(1, 7).reshape(2, 3)
print(array3)
subset = array3[:, :2]
print(subset)
subset[0, 0] = 1000
print(subset)
print(array3)
