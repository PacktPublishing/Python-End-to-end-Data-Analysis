#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

# Series
# ======

s1 = pd.Series(np.random.rand(4), index=['a', 'b', 'c', 'd'])
print(s1)

s2 = pd.Series(np.random.rand(4))
print(s2)

print(s1['c'])
s1['c'] = 3.14
s1[['c', 'a', 'b']]

s3 = pd.Series({'001': 'Nam', '002': 'Mary', '003': 'Peter'})
print(s3)

s4 = pd.Series({'001': 'Nam', '002': 'Mary', '003': 'Peter'}, index=['002', '001', '024', '065'])
print(s4)

pd.isnull(s4)

s5 = pd.Series(2.71, index=['x', 'y'])
print(s5)

s6 = pd.Series(np.array([2.71, 3.14]), index=['z', 'y'])
print(s6)

print(s5 + s6)


# DataFrame
# =========

data = {'Year': [2000, 2005, 2010, 2014],
        'Median_Age': [24.2, 26.4, 28.5, 30.3],
        'Density': [244, 256, 268, 279]}

df1 = pd.DataFrame(data)
print(df1)

df2 = pd.DataFrame(data, columns=['Year', 'Density', 'Median_Age'])
print(df2)

df3 = pd.DataFrame(data, columns=['Year', 'Density', 'Median_Age'],
                   index=['a', 'b', 'c', 'd'])

print(df3.index)

df4 = pd.DataFrame([
        ['Peter', 16, 'pupil', 'TN', 'M', None],
        ['Mary', 21, 'student', 'SG', 'F', None],
        ['Nam', 22, 'student', 'HN', 'M', None],
        ['Mai', 31, 'nurse', 'SG', 'F', None],
        ['John', 28, 'laywer', 'SG', 'M', None]
    ], columns=['name', 'age', 'career', 'province', 'sex', 'award'])

print(df4.name)

df4['award'] = None
print(df4)

print(df4.ix[1])

df4 = pd.read_csv('person.csv')
print(df4)

# Reindexing and altering labels
# ==============================

s2.reindex([0, 2, 'b', 3])
print(s2)

df1.reindex(index=[0, 2, 'b', 3], columns=['Density', 'Year', 'Median_Age', 'C'])

# Head and Tail
# =============

s7 = pd.Series(np.random.rand(10000))
print(s7.head())
print(s7.tail(3))

# Binary operations
# =================

df5 = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['a', 'b', 'c'])
print(df5)

df6 = pd.DataFrame(np.arange(8).reshape(2, 4), columns=['a', 'b', 'c', 'd'])
print(df6)

print(df5 + df6)

df7 = df5.add(df6, fill_value=0)
print(df7)

print(df5.eq(df6))

# Functional statistics
# =====================

print(df5.sum())
print(df7.sum(skipna=False))
print(df5.describe())
print(df5.describe(percentiles=[0.5, 0.8]))


# Function application
# ====================

print(df5.apply(np.std, axis=1))

fun = lambda x: x.max() - x.min()
print(df5.apply(fun, axis=1))

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(x))

# Sorting
# =======

df7 = pd.DataFrame(np.arange(12).reshape(3, 4), 
                   columns=['b', 'd', 'a', 'c'],
                   index=['x', 'y', 'z'])

print(df7)
print(df7.sort_index(axis=1))

print(s4.order(na_position='first'))

s4.sort(na_position='first')
print(s4)

print(df7.sort(['b', 'd'], ascending=False))

# Indexing and selecting data
# ===========================

print(s4[['024', '002']])

s4[['024', '002']] = 'unknown'
print(s4)

print(df5[['b', 'c']])
print(df5.ix[0])
print(df5.ix[0, 1:3])

# Computational tools
# ===================

s1 = pd.Series(np.random.rand(3))
print(s1)

s2 = pd.Series(np.random.rand(3))
print(s2)

print(s1.cov(s2))

df8 = pd.DataFrame(np.random.rand(12).reshape(4, 3),
                   columns=['a', 'b', 'c'])

print(df8)
print(df8.cov())
print(df8.corr(method='spearman'))

df9 = pd.DataFrame(np.arange(8).reshape(4, 2), columns=['a', 'b'])
print(df9)

print(df8.corrwith(df9))

# Working with missing data
# =========================

df8 = pd.DataFrame(np.arange(12).reshape(4, 3), columns=['a', 'b', 'c'])
print(df8)

df9 = df8.reindex(columns=['a', 'b', 'c', 'd'])
print(df9)

df10 = df8.reindex([3, 2, 'a', 0])
print(df10)
print(df10.isnull())

s4 = pd.Series({'001': 'Nam', '002': 'Mary', '003': 'Peter'}, index=['002', '001', '024', '065'])
print(s4)
print(s4.dropna())

print(df9.dropna())
print(df9.dropna(axis=1))

df11 = df8.reindex([3, 2, 'a', 0], fill_value=0)
print(df11)
print(df9.fillna(-1))

# Advanced uses of Pandas for data analysis
# =========================================

s8 = pd.Series(np.random.rand(8), index=[
        ['a','a','b','b','c','c', 'd','d'],
        [0, 1, 0, 1, 0,1, 0, 1, ]])
print(s8)
print(s8.unstack())

df = pd.DataFrame(np.random.rand(12).reshape(4, 3),
                  index=[['a', 'a', 'b', 'b'], [0, 1, 0, 1]],
                  columns=[['x', 'x', 'y'], [0, 1, 0]])

print(df)
print(df.index)
print(df.columns)

print(df['x'])
print(df[[0]])
print(df.ix['a', 'x'])
print(df.ix['a', 'x'].ix[1])

print(df.std(level=1))
print(df.std(level=0))

# Panel data
# ==========

panel = pd.Panel(np.random.rand(2, 4, 5), items=['item1', 'item2'])
print(panel)

df1 = pd.DataFrame(np.arange(12).reshape(4, 3), columns=['a', 'b', 'c'])
print(df1)

df2 = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['a', 'b', 'c'])
print(df2)

panel2 = pd.Panel({'item1': df1, 'item2': df2})
print(panel2)

print(panel2['item1'])
print(panel2.ix[:, 1:3, ['b', 'c']])
