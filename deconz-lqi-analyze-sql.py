#!/usr/bin/env python3

import datetime
import itertools
import sys

from collections import defaultdict


TIMESTAMP_PATTERN = '%d.%m.%Y %H:%M:%S'


lqi_by_date_and_device = defaultdict(dict)
with open(sys.argv[1], 'rt') as f:
  for line in f:
    # Some input lines contain the date, others a pipe separated SQL output.
    if '|' in line:
      ts_str, src, neighbor, lqi_str = line.split('|')
      ts = datetime.datetime.strptime(ts_str, TIMESTAMP_PATTERN)
      lqi = int(lqi_str)
      lqi_by_date_and_device[ts][neighbor] = lqi

all_devices = sorted(set(itertools.chain(
    *[v.keys() for v in lqi_by_date_and_device.values()])))
sorted_dates = sorted(lqi_by_date_and_device.keys())
print('Date;' + ';'.join(all_devices))
for date in sorted_dates:
  cols = [date] + [lqi_by_date_and_device[date].get(d, '') for d in all_devices]
  print(';'.join([str(c) for c in cols]))
