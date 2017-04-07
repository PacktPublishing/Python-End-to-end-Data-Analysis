#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(5)
Y = 3.14 + 2.71 * np.random.rand(5)

plt.subplots(2)

plt.subplot(211)
plt.bar(X, Y, align='center', alpha=0.4, color='y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('bar plot in vertical')

plt.subplot(212)
plt.barh(X, Y, align='center', alpha=0.4, color='c')
plt.xlabel('x')
plt.ylabel('y')
plt.title('bar plot in horizontal')

plt.savefig('bar.png')
