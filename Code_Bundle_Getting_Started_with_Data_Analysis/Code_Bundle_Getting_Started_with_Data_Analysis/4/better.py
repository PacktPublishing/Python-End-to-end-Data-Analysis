#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 6)
y = np.power(x, 2)

plt.axis([0, 6, 0, 10])
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Visualization using Pyplot from Matplotlib')

plt.savefig('better.png')
