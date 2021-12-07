#!/usr/bin/python3
filename = 'input/day6.txt'
ages = {}
with open(filename) as file:
    for age in file.read().split(','): 
        ages[int(age)] = ages.get(int(age), 0) + 1

for day in range(256):
    temp = {}
    temp[6] = temp[8] = ages.get(0, 0)
    for y in range(1, 9):
        temp[y-1] = temp.get(y-1, 0) + ages.get(y, 0)
    ages = temp
print(sum(ages.values()))