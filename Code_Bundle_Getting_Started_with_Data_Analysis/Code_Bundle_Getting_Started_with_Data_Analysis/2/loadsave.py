#!/usr/bin/env python
# coding: utf-8

# Saving
a = np.array([[0, 1, 2], [3, 4, 5]])
np.save('test1.npy', a)

a = np.arange(4)
b = np.arange(7)

np.savez('test2.npz', arr0=a, arr1=b)

# Loading
dic = np.load('test2.npz')
print(dic['arr0'])

x = np.arange(4)
np.savetxt('test3.out', x, delimiter=',')

print(np.load('test1.npy'))
print(np.loadtxt('test3.out', delimiter=','))

