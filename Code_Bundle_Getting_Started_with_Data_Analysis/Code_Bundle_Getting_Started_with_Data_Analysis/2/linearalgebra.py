#!/usr/bin/env python
# coding: utf-8

import numpy as np

A = np.array([[1, 4, 6],
              [5, 2, 2],
              [-1, 6, 8]])

w, v = np.linalg.eig(A)
print(w)
print(v)

A = np.array([[1, 4, 6], [5, 2, 2], [-1, 6, 8]])
b = np.array([[1], [2], [3]])
x = np.linalg.solve(A, b)
print(x)

