#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.4, 0.4, 20)
y = x * x + 2 * x + 1
plt.plot(x, y, 'c', linewidth=2.0)
plt.text(-1.5, 1.8, 'y=x^2 + 2*x + 1',
    fontsize=14, style='italic')
plt.annotate('minima point', xy=(-1, 0),
    xytext=(-1, 0.3), horizontalalignment='center',
    verticalalignment='top', 
    arrowprops=dict(arrowstyle='->', 
        connectionstyle='arc3'))
 
plt.savefig('annotate.png')