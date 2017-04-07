#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 6)
y = np.power(x, 2)

plt.plot(x*2, 'g^', x*3, 'rs', x**x, 'y-')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot y value without given x values')
plt.axis([0, 6, 0, 30])
plt.savefig('line.png')
