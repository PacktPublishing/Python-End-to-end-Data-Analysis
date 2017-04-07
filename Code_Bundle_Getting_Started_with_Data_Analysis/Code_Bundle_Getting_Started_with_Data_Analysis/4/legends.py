#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20);
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
plt.plot(x, y1, 'c', label='y=sin(x)')
plt.plot(x, y2, 'y', label='y=cos(x)')
plt.plot(x, y3, 'r', label='y=tan(x)')
plt.legend(loc='upper left')
plt.savefig('legends.png')
