#!/usr/bin/env python

"""

Support code for "Filtering" subsection in Chapter 7.

"(1987, 5, 20, 0, 0, 0)","18.63"
"(1987, 5, 21, 0, 0, 0)","18.45"
"(1987, 5, 22, 0, 0, 0)","18.55"
"""

import datetime
import pandas as pd

def convert_date(s):
    parts = s.replace("(", "").replace(")", "").split(",")
    if len(parts) < 6:
        return datetime.date(1970, 1, 1)
    return datetime.datetime(*[int(p) for p in parts])

if __name__ == '__main__':
    df = pd.read_csv("rbrted.csv", sep=',', names=["date", "price"], converters={"date": convert_date}).dropna()
    df.to_csv('rbrted_cleaned.csv', columns=["date", "price"], index=False)
