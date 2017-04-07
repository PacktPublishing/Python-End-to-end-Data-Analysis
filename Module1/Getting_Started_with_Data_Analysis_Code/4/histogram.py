#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

mu = 100
sigma = 25
fig, (ax0, ax1) = plt.subplots(ncols = 2)
x = mu + sigma * np.random.randn(1000)
ax0.hist(x, 20, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
ax0.set_title('Stepfilled histogram')
ax1.hist(x, bins=[100,150, 165, 170, 195], normed=1, histtype='bar', rwidth=0.8)
ax1.set_title('uniquel bins histogram')
plt.tight_layout()	#automatically adjust subplot parameters to give specified padding
plt.savefig('histogram.png')
