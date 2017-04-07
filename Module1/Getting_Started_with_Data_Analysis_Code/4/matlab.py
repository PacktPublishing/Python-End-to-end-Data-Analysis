#!/usr/bin/env python2

from numpy import *
from matplotlib.pyplot import *

x = linspace(0, 3, 6)
y = power(x, 2)

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('Data visualization with MATLAB-like API')

savefig('matlab.png')

