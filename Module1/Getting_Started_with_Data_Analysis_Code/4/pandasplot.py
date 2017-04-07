#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.random.normal(10, 8, 20))
s.plot(style='ko-', alpha=0.4, label='Series plotting')
plt.legend()

plt.savefig('pandasplot.png')

