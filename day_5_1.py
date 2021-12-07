#!/usr/bin/python3
filename = 'input/day5.txt'
with open(filename) as file:
    positions = [[[int(position) for position in coordinates.split(',')] for coordinates in line.split('->')] for line in file.read().splitlines()]
    vents = {}
    for longitude, latitude in filter(lambda pos: pos[0][0] == pos[1][0] or pos[0][1] == pos[1][1], positions):
        for x in range(min(longitude[0], latitude[0]), max(longitude[0], latitude[0]) + 1):
            for y in range(min(longitude[1], latitude[1]), max(longitude[1], latitude[1]) + 1):
                vents[(x,y)] = (vents[(x,y)] + 1) if (x,y) in vents else 1
    print(len(list(filter(lambda c: int(c[1]) >= 2, vents.items()))))
