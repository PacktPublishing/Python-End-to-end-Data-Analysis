#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

s = pd.Series(np.random.normal(10, 8, 20))
s.plot(style='ko-', alpha=0.4)
plt.legend(['Series plotting'])

plt.savefig('series.png')
