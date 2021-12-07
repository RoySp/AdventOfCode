#!/usr/bin/python3
filename = 'input/day7.txt'
with open(filename) as file:
    crabs = [int(n) for n in file.read().split(',')]

def calculate_fuel_cost(crabs, average):
    return sum(abs(average - c) * (abs(average - c) + 1) // 2 for c in crabs)

average = sum(crabs) // len(crabs)
fuel_cost = min(calculate_fuel_cost(crabs, average), calculate_fuel_cost(crabs, average + 1))

print(fuel_cost)