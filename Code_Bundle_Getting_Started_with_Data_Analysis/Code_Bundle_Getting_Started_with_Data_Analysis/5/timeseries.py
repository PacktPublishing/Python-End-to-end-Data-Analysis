#!/usr/bin/env python
# coding: utf-8

import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytz
import random

# Date and Time
# =============

print(datetime.datetime(2000, 1, 1))
print(datetime.datetime.strptime("2000/1/1", "%Y/%m/%d"))
print(datetime.datetime(2000, 1, 1, 0, 0).strftime("%Y%m%d"))

# to_datetime
# ===========

print(pd.to_datetime("4th of July"))
print(pd.to_datetime("13.01.2000"))
print(pd.to_datetime("7/8/2000"))
print(pd.to_datetime("7/8/2000", dayfirst=True))
print(issubclass(pd.Timestamp, datetime.datetime))

ts = pd.to_datetime(946684800000000000)

print(ts.year, ts.month, ts.day, ts.weekday())

index = [pd.Timestamp("2000-01-01"),
         pd.Timestamp("2000-01-02"),
         pd.Timestamp("2000-01-03")]

ts = pd.Series(np.random.randn(len(index)), index=index)
print(ts)
print(ts.index)

ts = pd.Series(np.random.randn(len(index)),
               index=["2000-01-01", "2000-01-02", "2000-01-03"])
print(ts.index)

index = pd.to_datetime(["2000-01-01", "2000-01-02", "2000-01-03"])
ts = pd.Series(np.random.randn(len(index)), index=index)
print(ts.index)

print(pd.date_range(start="2000-01-01", periods=3, freq='H'))
print(pd.date_range(start="2000-01-01", periods=3, freq='T'))
print(pd.date_range(start="2000-01-01", periods=3, freq='S'))
print(pd.date_range(start="2000-01-01", periods=3, freq='B'))
print(pd.date_range(start="2000-01-01", periods=5, freq='1D1h1min10s'))
print(pd.date_range(start="2000-01-01", periods=5, freq='12BH'))

bh = pd.tseries.offsets.BusinessHour(start='07:00', end='22:00')
print(bh)


print(pd.date_range(start="2000-01-01", periods=5, freq=12 * bh))
print(pd.date_range(start="2000-01-01", periods=5, freq='W-FRI'))
print(pd.date_range(start="2000-01-01", periods=5, freq='WOM-2TUE'))


s = pd.date_range(start="2000-01-01", periods=10, freq='BAS-JAN')
t = pd.date_range(start="2000-01-01", periods=10, freq='A-FEB')
s.union(t)
index = pd.date_range(start='2000-01-01', periods=200, freq='B')
print(index)

ts = pd.Series(np.random.randn(len(index)), index=index)
walk = ts.cumsum()
walk.plot()
plt.savefig('random_walk.png')

print(ts.head())
print(ts[0])
print(ts[1:3])
print(ts['2000-01-03'])
print(ts[datetime.datetime(2000, 1, 3)])
print(ts['2000-01-03':'2000-01-05'])
print(ts['2000-01-03':datetime.datetime(2000, 1, 5)])
print(ts['2000-01-03':datetime.date(2000, 1, 5)])
print(ts['2000-02'])
print(ts['2000-03':'2000-05'])

small_ts = ts['2000-02-01':'2000-02-05']

print(small_ts)
print(small_ts.shift(2))
print(small_ts.shift(-2))

# Downsampling
# ============

rng = pd.date_range('4/29/2015 8:00', periods=600, freq='T')
ts = pd.Series(np.random.randint(0, 100, len(rng)), index=rng)

print(ts.head())
print(ts.resample('10min').head())
print(ts.resample('10min', how='sum').head())
print(ts.resample('1h', how='sum').head())
print(ts.resample('1h', how='max').head())


print(ts.resample('1h', how=lambda m: random.choice(m)).head())
print(ts.resample('1h', how='ohlc').head())

# Upsampling
# ==========

rng = pd.date_range('4/29/2015 8:00', periods=10, freq='H')
ts = pd.Series(np.random.randint(0, 100, len(rng)), index=rng)

print(ts.head())
print(ts.resample('15min'))
print(ts.head())
print(ts.resample('15min', fill_method='ffill').head())
print(ts.resample('15min', fill_method='bfill').head())
print(ts.resample('15min', fill_method='ffill', limit=2).head())
print(ts.resample('15min', fill_method='ffill', limit=2, loffset='5min').head())

tsx = ts.resample('15min')
print(tsx.interpolate().head())

# Time zone handling
# ==================

t = pd.Timestamp('2000-01-01')
print(t.tz is None)

t = pd.Timestamp('2000-01-01', tz='Europe/Berlin')
print(t.tz)

rng = pd.date_range('1/1/2000 00:00', periods=10, freq='D', tz='Europe/London')
print(rng)


tz = pytz.timezone('Europe/London')
rng = pd.date_range('1/1/2000 00:00', periods=10, freq='D', tz=tz)
print(rng)

rng = pd.date_range('1/1/2000 00:00', periods=10, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts.index.tz is None)

ts_utc = ts.tz_localize('UTC')

print(ts_utc.index.tz)
print(ts_utc.tz_convert('Europe/Berlin').index.tz)
print(ts_utc.tz_convert(None).index.tz is None)
print(ts_utc.tz_localize(None).index.tz is None)

# Time deltas
# ===========

print(pd.Timedelta('1 days'))
print(pd.Timedelta('-1 days 2 min 10s 3us'))
print(pd.Timedelta(days=1,seconds=1))
print(pd.Timedelta(days=1) + pd.Timedelta(seconds=1))
print(pd.to_timedelta('20.1s'))
print(pd.to_timedelta(np.arange(7), unit='D'))

# Time series plotting
# ====================

rng = pd.date_range(start='2000', periods=120, freq='MS')
ts = pd.Series(np.random.randint(-10, 10, size=len(rng)), rng).cumsum()

print(ts.head())

plt.clf()
ts.plot(c='k', title='Example time series')
plt.savefig('time_series_1.png')

ts.resample('2A').plot(c='0.75', ls='--')
ts.resample('5A').plot(c='0.25', ls='-.')

plt.clf()

tsx = ts.resample('1A')
ax = tsx.plot(kind='bar', color='k')
plt.savefig('time_series_2.png')

ax.set_xticklabels(tsx.index.year)
plt.clf()
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot(color=['k', '0.75', '0.5', '0.25'], ls='--')
plt.savefig('time_series_3.png')
