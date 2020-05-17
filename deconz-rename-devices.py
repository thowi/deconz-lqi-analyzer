#!/usr/bin/env python3

import csv
import re
import sys


def load_names(filename):
  names = {}
  with open(filename, 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
      addr, name, vendor, type = row
      names[addr] = name
  return names


names_filename, edit_filename = sys.argv[1:3]
names = load_names(names_filename)
rep = dict((re.escape(k), v) for k, v in names.items())
pattern = re.compile('|'.join(rep.keys()))
with open(edit_filename, 'rt') as f:
  for line in f:
    print(pattern.sub(lambda m: rep[re.escape(m.group(0))], line), end='')
