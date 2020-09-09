#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    items.sort(key=lambda item: item.value, reverse=True)

    sack = []
    value = 0
    sack_weight = 0
    max_weight = 50
    for item in items:
        if sack_weight + item.weight < max_weight:
          sack.append(item)
          sack_weight += item.weight
          value += item.value            

    return (sack, sack_weight, value)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
