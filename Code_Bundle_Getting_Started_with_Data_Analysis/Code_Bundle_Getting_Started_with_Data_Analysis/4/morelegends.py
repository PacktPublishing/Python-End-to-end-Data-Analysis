#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20);
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

p1 = plt.plot(x, y1, 'c', label='y=sin(x)')
p2 = plt.plot(x, y2, 'y', label='y=cos(x)')
p3 = plt.plot(x, y3, 'r', label='y=tan(x)')

lsin = plt.legend(handles=p1, loc='lower right')
lcos = plt.legend(handles=p2, loc='upper left')
ltan = plt.legend(handles=p3, loc='upper right')

fig = plt.gcf()

fig.gca().add_artist(lsin)
fig.gca().add_artist(lcos)

plt.tight_layout()

plt.savefig('morelegends.png')
