#!/usr/bin/env python
# coding: utf-8

"""
Numpy arrays
"""

import numpy as np

p = np.array([48.858598, 2.294495])
print(p.ndim)
print(p.shape)
print(p.dtype)

# Data type
a = np.array([1, 2, 3, 4])
print(a.dtype)

float_b = a.astype(np.float64)
print(float_b.dtype)

# Array creation
a = np.arange(7)
print(a)
print(a[1], a[4], a[-1])

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[0, 2])

a[0, 2] = 10
print(a)

b = a[2]
print(b)

c = a[:2]
print(c)

b[-1] = 11
print(a)

# Fancy indexing
a = np.array([3, 5, 1, 10])
b = (a % 5 == 0)
print(b)

c = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])
print(c[b])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(a[[2, 1]])
print(a[[-2, -1]])
print(a[[2, 3], [0, 1]])

# Numerical operations on arrays
a = np.ones(4)
print(a * 2)
print(a + 3)

a = np.ones([2, 4])
print(a * a)
print(a + a)

a = np.array([1, 2, 3, 4])
b = np.array([1, 1, 5, 3])

print(a == b)
print(np.array_equal(a, b))

c = np.array([1, 0])
d = np.array([1, 1])
print(np.logical_and(c, d))

# Array functions
a = np.array([[0, 5, 10], [20, 25, 30]])
print(a.reshape(3, 2))
print(a.T)

a = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print(a.swapaxes(1, 2))

a = np.array([[1, 2, 3],[4,5,6]])
print(np.dot(a.T, a))

a = np.array ([[6, 34, 1, 6], [0, 5, 2, -1]])
print(np.sort(a))
print(np.sort(a, axis=0))

b = np.argsort(a)
print(b)
print(a[0][b[0]])
print(np.argmax(a))