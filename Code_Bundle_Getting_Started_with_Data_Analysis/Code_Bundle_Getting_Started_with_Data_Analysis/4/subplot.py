#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 6)
y = np.power(x, 2)

plt.figure('a')

plt.subplot(221)
plt.plot(y + y, 'r--')

plt.subplot(222)
plt.plot(y * 3, 'ko')

plt.subplot(223)
plt.plot(y * y, 'b^')

plt.subplot(224)

# alter things after the fact
plt.figure('a')
plt.subplot(222)
plt.title('Visualization of y * 3')

plt.savefig('subplot.png')
