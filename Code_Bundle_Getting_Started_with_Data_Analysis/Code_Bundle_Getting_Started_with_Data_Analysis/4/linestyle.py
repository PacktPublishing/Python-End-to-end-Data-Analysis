#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 6)
y = np.power(x, 2)

line, = plt.plot(y, color='red', linewidth=2.0)
line.set_linestyle('--')
plt.setp(line, marker='o')

plt.savefig('linestyle.png')
