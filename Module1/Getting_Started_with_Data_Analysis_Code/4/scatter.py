#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

X = np.random.normal(0, 1, 1000)
Y = np.random.normal(0, 1, 1000)

plt.scatter(X, Y, c=['b', 'g', 'k', 'r', 'c'])
# s = np.random.randint(10, 100)
plt.savefig('scatter.png')
