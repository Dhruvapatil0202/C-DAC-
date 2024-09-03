import numpy as np
# x = [-1.1, 0.0, 3.6, -7.2]
# x = np.array(x)
# print(x[2])
#
# x[2] = 20
# print(x[2])
#
# y = x
# x[2] = 20.0
# print(y)
#
# y = x.copy()
# y[3] = 9.0
# print(x==y)

# x, y = np.array([1, -2]), np.array([1, 1, 0])
# z = np.concatenate((x, y))
# z2 = np.concatenate((y, x))
#
# print(z, z2)

# x = np.array([1, 8, 3, 2, 1, 9, 7])
# d = x[1:] - x[:-1]
# print(d)



# Array is considered as a vector
# Tuple is not a Vector

# List of vectors

x = np.array([1,2])
y = np.array([1,-2])
z = np.array([0,1])

list_of_vectors = [x,y,z]
print(list_of_vectors[1])