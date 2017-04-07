#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 6)
y = np.power(x, 2)

# another figure
plt.figure('b')
ax1 = plt.axes([0.05, 0.1, 0.4, 0.32])
ax2 = plt.axes([0.52, 0.1, 0.4, 0.32])
ax3 = plt.axes([0.05, 0.53, 0.87, 0.44])

plt.savefig('subs.png')
