filename = 'input/day1.txt'
with open(filename) as file:
    lines = file.readlines()
    depths = [int(line.rstrip()) for line in lines]

window_size = 3
depthSums = []
for i in range(len(depths) - window_size + 1):
    depthSums.append(sum(depths[i: i + window_size]))

increased = 0
for index, depth in enumerate(depthSums): 
    if index != 0 :
        if depthSums[index - 1] < depth :
            increased +=1 

print(increased)
