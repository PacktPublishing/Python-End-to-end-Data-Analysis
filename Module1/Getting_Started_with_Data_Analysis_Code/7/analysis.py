#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

# Cleaning
# ========

df = pd.read_csv("small.csv")
print(df)

df = pd.read_csv("small.csv", header=None)
print(df)

df = pd.read_csv("small.csv", names=["age", "height"])
print(df)

print(df.age.dtype)
print(df.height.dtype)
try:
    print(df.height.astype('float'))
except ValueError as err:
    print(err)

print(df.height.convert_objects(convert_numeric=True))

remove_stars = lambda s: s.replace("*", "")
df = pd.read_csv("small.csv", names=["age", "height"],
                 converters={"height": remove_stars})

print(df)
df.height = df.height.convert_objects(convert_numeric=True)
print(df)

print(df.dropna())
print(df.fillna(5.0))
print(df.fillna(df.height.mean()))

# Filtering
# =========

df = pd.read_csv("rbrted_cleaned.csv")

print(df.head())
print(df.tail())
print(df[df.price==df.price.min()])
print(df[df.price==df.price.max()])
print(np.abs(df.price - df.price.mean()))
print(df[np.abs(df.price - df.price.mean()) > 2.5 * df.price.std()])

df.index = df.date
del df["date"]

print(df.head())

decade = df["1980":"1989"]
print(decade[np.abs(decade.price - decade.price.mean()) > 2.5 * decade.price.std()])

decade = df["1990":"1999"]
print(decade[np.abs(decade.price - decade.price.mean()) > 5 * decade.price.std()])

# Merging
# =======

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df1)

df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})
print(df2)

print(df1.append(df2))
print(df1.append(df2, ignore_index=True))
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))
print(pd.concat([df1, df2], keys=['UK', 'DE']))

df3 = pd.concat([df1, df2], keys=['UK', 'DE'])

print(df3.ix["UK"])

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': range(4)})
print(df1)

df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],
                    'value': range(10, 14)})
print(df2)

print(df1.merge(df2, on='key'))
print(df1.merge(df2, on='key', how='left'))
print(df1.merge(df2, on='key', how='right'))
print(df1.merge(df2, on='key', how='outer'))

# Grouping Data
# =============

df = pd.read_csv('cities.tsv', sep='\t', names=['date', 'city', 'value'])
print(df)
print(df.groupby("city").groups)

grouped = df.groupby(["city", "value"])

print(grouped["value"].max())
print(grouped["value"].sum())
print(df['value'].groupby(df['city']).sum())

# Reshaping
# =========

print(df)
print(df.groupby('city').max())
pv = df.pivot("date", "city", "value")
print(pv)

print(pv.max())
print(pv.max(axis=1))

df = pd.read_csv("sunshine.tsv", sep='\t', names=['country', 'city', 'date', 'hours'])

print(df.head())
print(df.groupby("city").describe())
print(df.groupby(["country", "date"]).describe())
print(df.groupby("city").mean())
print(df.groupby("city").agg(np.mean))
print(df.groupby("city").agg(lambda s: abs(min(s) - max(s))))
