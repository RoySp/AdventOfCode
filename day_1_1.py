#!/usr/bin/python3
filename = 'input/day1.txt'
with open(filename) as file:
    lines = file.readlines()
    depths = [int(line.rstrip()) for line in lines]

increased = 0
for index, depth in enumerate(depths): 
    if index != 0 :
        if depths[index - 1] < depth :
            increased += 1
print(increased)
