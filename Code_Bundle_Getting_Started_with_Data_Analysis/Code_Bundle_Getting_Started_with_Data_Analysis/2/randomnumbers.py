#!/usr/bin/env python
# coding: utf-8

import numpy as np

np.random.seed(20)
print(np.random.rand(5))
print(np.random.rand(5))

np.random.seed(20)
print(np.random.rand(5))

print(np.random.randint(10, 20, 5))

a = np.arange(10)
np.random.shuffle(a)
print(a)

