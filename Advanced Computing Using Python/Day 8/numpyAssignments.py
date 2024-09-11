
import numpy as np
# Assignment 3
# matrix1 = np.random.randint(1,11, size=(3,3))
# transpose = matrix1.transpose()
# print(matrix1)
# print(transpose)

# array_1d  = np.array([1,4,7])
# print(f"Size {a}")

def describeArray(matrix):
    print(matrix)
    print(f"Dimensions: {matrix.ndim}")
    print(f"Shape: {matrix.shape}")
    print(f"Size: {matrix.size}\n\n")

matrix_1d = np.array([2,5,6,9])
matrix2d = np.array([[2,5,6,9],[4,4,4,4]])
matrix_3d = np.array([[[2,5],[6,9]],[[4,4],[4,4]], [[4,6],[6,23]],[[6,0],[1,5]]])

describeArray(matrix_1d)
describeArray(matrix2d)
describeArray(matrix_3d)