#!/usr/bin/env python

import csv
import datetime
import itertools
import os.path
import re
import sys

import networkx as nx


NAMES_FILENAME = 'lqi-names.csv'
LQI_FILENAME_PATTERN = re.compile(
    r'lqi-(\d\d\d\d-\d\d-\d\d-\d\d-\d\d-\d\d).csv')
LQI_FILENAME_DATE_FORMAT = '%Y-%m-%d-%H-%M-%S'


def get_best_connection_to_node(graph, root, node):
  paths = nx.all_simple_paths(graph, root, node)
  return max([get_min_weight(graph, p) for p in paths])


def get_best_connection_to_all_nodes(graph, root):
  for node in graph.nodes:
    if node != root:
      yield node, get_best_connection_to_node(graph, root, node)


def get_min_weight(graph, path):
  min_weight = sys.maxsize
  for edge in [tuple(path[i:i+2]) for i in range(len(path) - 1)]:
    min_weight = min(min_weight, graph.edges[edge]['weight'])
  return min_weight


def get_coordinator_and_graph_for_csv_file(filename):
  g = nx.Graph()
  coordinator = None
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
      src, neighbor, neighbor_pan_id, relationship, lqi, depth = row
      if not coordinator:
        # The coordinator is the neighbor of the first node.
        coordinator = neighbor
      if relationship == 'none':
        continue
      parent, child = src, neighbor
      g.add_edge(parent, child, weight=int(lqi))
  return coordinator, g


def load_names(filename):
  names = {}
  with open(filename, 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
      addr, name, vendor, type = row
      names[addr] = name
  return names


def main(argv=None):
  names = {}
  best_connection_by_time_and_node = {}
  if argv is None:
    argv = sys.argv
  for filename in argv[1:]:
    path, name = os.path.split(filename)
    if name == NAMES_FILENAME:
      names = load_names(filename)
    else:
      match = LQI_FILENAME_PATTERN.match(name)
      if match:
        file_datetime = datetime.datetime.strptime(
            match.group(1), LQI_FILENAME_DATE_FORMAT)
        best_connection_by_time_and_node[file_datetime] = {}
        coord, graph = get_coordinator_and_graph_for_csv_file(filename)
        for node, lqi in list(get_best_connection_to_all_nodes(graph, coord)):
          best_connection_by_time_and_node[file_datetime][node] = lqi

  best = best_connection_by_time_and_node
  all_nodes = sorted(set(itertools.chain(*[v.keys() for v in best.values()])))
  sorted_dates = sorted(best.keys())
  print('Date;' + ';'.join([names.get(n, n) for n in all_nodes]))
  for date in sorted_dates:
    cols = [date] + [best[date].get(n, '') for n in all_nodes]
    print(';'.join([str(c) for c in cols]))


if __name__ == '__main__':
  sys.exit(main())
