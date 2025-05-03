import numpy as np
import matplotlib.pyplot as plt

array1 = np.array([1,2,3])
print(array1)
array2 = np.array([[1,2,3],[4,5,6]])
print(array2)
array3 = np.array([[[1,2,3],[4,5,6]]])
print(array3)

print(array1.ndim)
print(array2.ndim)
print(array3.ndim)

print(array1.shape)
print(array2.shape)
print(array3.shape)

print(array1.dtype)
print(array2.dtype)
print(array3.dtype)

print(array1.itemsize)
print(array2.itemsize)
print(array3.itemsize)

array5 = np.array([1,2,3], dtype=float)
array6 = np.zeros((2,3))
print(array6)
print(array5)

array7 = np.ones((2,4))
print(array7)

array8 = np.arange(-2,28,2)
print(array8)