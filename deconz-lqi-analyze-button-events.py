#!/usr/bin/env python3

import datetime
import itertools
import re
import sys

from collections import defaultdict


LOG_PATTERN = re.compile(r'([\d:]+).*uniqueid":"([\da-f:]+).*')


num_presses_by_time_and_device = defaultdict(lambda: defaultdict(int))
with open(sys.argv[1], 'rt') as f:
  for line in f:
    match = LOG_PATTERN.match(line)
    if match:
      timestamp, id_hex = match.groups()
      ts = timestamp[:6]
      num_presses_by_time_and_device[ts][id_hex] += 1

all_devices = sorted(set(itertools.chain(
    *[v.keys() for v in num_presses_by_time_and_device.values()])))
sorted_dates = sorted(num_presses_by_time_and_device.keys())
print('Date;' + ';'.join(all_devices))
for date in sorted_dates:
  cols = [date] + [num_presses_by_time_and_device[date].get(d, '') for d in all_devices]
  print(';'.join([str(c) for c in cols]))
