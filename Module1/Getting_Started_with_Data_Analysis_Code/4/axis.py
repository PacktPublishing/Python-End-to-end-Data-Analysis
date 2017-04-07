#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 6)
y = np.power(x, 2)

plt.plot(y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot y value without given x values')
plt.axis([0, 7, 0, 10])
plt.savefig('axis.png')
