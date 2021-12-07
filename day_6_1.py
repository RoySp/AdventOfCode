#!/usr/bin/python3
filename = 'input/day6.txt'
with open(filename) as file:
    ages = [int(n) for n in file.read().split(',')]

a = ages
for day in range(80):
    old_fish = ages.count(0)
    ages = [a-1 if a != 0 else 6 for a in ages]
    new_fish = [8] * old_fish
    ages.extend(new_fish)
print(len(ages))