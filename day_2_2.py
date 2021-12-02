filename = 'input/day2.txt'
with open(filename) as file:
    lines = file.readlines()
    commands = [line.rstrip() for line in lines]

depth = 0
horizontal = 0
aim = 0

for command in commands:
    splitted = command.split()
    movement = splitted[0]
    steps = int(splitted[1])
    if(movement == "forward"):
        horizontal += steps
        depth += steps * aim
    elif(movement == "down"):
        aim += steps
    elif(movement == "up"):
        aim -= steps

print(horizontal * depth)
