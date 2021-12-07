#!/usr/bin/python3
filename = 'input/day5.txt'
with open(filename) as file:
    positions = [[[int(position) for position in coordinates.split(',')] for coordinates in line.split('->')] for line in file.read().splitlines()]
    vents = {}
    for start_position, end_position in filter(lambda pos: pos[0][0] == pos[1][0] or pos[0][1] == pos[1][1], positions):
        for longitude in range(min(start_position[0], end_position[0]), max(start_position[0], end_position[0]) + 1):
            for latitude in range(min(start_position[1], end_position[1]), max(start_position[1], end_position[1]) + 1):
                vents[(longitude, latitude)] = (vents[(longitude, latitude)] + 1) if (longitude, latitude) in vents else 1

    for start_position, end_position in filter(lambda pos: pos[0][0] != pos[1][0] and pos[0][1] != pos[1][1], positions):
        start, end = sorted([start_position, end_position], key = lambda x: x[0])
        diagonal = 1 if start[1] < end[1] else -1
        latitude = start[1]
        for longitude in range(start[0], end[0] + 1):
            vents[(longitude, latitude)] = (vents[(longitude, latitude)] + 1) if (longitude, latitude) in vents else 1
            latitude += diagonal

    print(len(list(filter(lambda c: int(c[1]) >= 2, vents.items()))))