#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 255)
y = np.linspace(-2, 2, 300)

z = np.sin(y[:, np.newaxis] * np.cos(x))

plt.contour(x, y, z, 255, linewidth=2)
plt.savefig('contour.png')
