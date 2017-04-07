#!/usr/bin/env python

"""
Support code for "Data aggregation" subsection in Chapter 7.

Create some artificial data.
"""

import datetime
import pandas as pd
import random

citymap = {
    'Germany': ['Hamburg', 'Munich', 'Berlin', 'Leipzig', 'Frankfurt'],
    'UK': ['London', 'Manchester', 'Glasgow', 'Birmingham', 'Edinburgh'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Nice', 'Bordeax'],
}

for country, cities in citymap.iteritems():
    for city in cities:
        for date in pd.date_range('2015-06-01', periods=10):
            row = [country, city, str(date.date()), str(random.randint(0, 10))]
            print("\t".join(row))

