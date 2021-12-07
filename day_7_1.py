#!/usr/bin/python3
filename = 'input/day7.txt'
with open(filename) as file:
    crabs = [int(n) for n in file.read().split(',')]

median = sorted(crabs)[len(crabs) // 2]
cost = sum(abs(median - c) for c in crabs)

print(cost)