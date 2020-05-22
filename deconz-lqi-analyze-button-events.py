#!/usr/bin/env python3

import datetime
import itertools
import re
import sys

from collections import defaultdict


LOG_PATTERN = re.compile(r'([\d:]+).*changed.*uniqueid":"([\da-f:]+).*')
TIMESTAMP_PATTERN = '%H:%M:%S:%f'


presses = []
with open(sys.argv[1], 'rt') as f:
  for line in f:
    match = LOG_PATTERN.match(line)
    if match:
      timestamp_str, id_hex = match.groups()
      timestamp = datetime.datetime.strptime(timestamp_str, TIMESTAMP_PATTERN)
      presses.append((timestamp, id_hex))

all_devices = sorted(set([p[1] for p in presses]))
sorted_presses = sorted(presses, key=lambda p: p[0])
last_press_by_device = {}
print('Date;' + ';'.join(all_devices))
for press in sorted_presses:
  timestamp, id_hex = press
  last_press = last_press_by_device.get(id_hex, timestamp)
  seconds_since = (timestamp - last_press).total_seconds()
  col_index = 1 + all_devices.index(id_hex)
  cols = [timestamp] + [seconds_since if d == id_hex else '' for d in all_devices]
  print(';'.join([str(c) for c in cols]))
  last_press_by_device[id_hex] = timestamp
