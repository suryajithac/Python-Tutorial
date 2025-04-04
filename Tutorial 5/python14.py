import numpy as np
array1 = np.random.randint(0, 20, (3, 3))
array2 = np.random.randint(0, 20, (3, 3))
print("Matrix Addition:")
print(array1 + array2)
print("Matrix Multiplication:")
print(array1 @ array2)
print("Transpose of Product Matrix:")
print((array1 @ array2).T)