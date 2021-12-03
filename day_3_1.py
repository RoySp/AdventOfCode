#!/usr/bin/python3
filename = 'input/day3.txt'
with open(filename) as file:
    lines = file.readlines()
    diagnostics = [line.rstrip() for line in lines]

def split(word):
    return [char for char in word]

bytes = {}
for i in range(len(diagnostics[0])) :
    bytes[i] = {0:0, 1:0}

for diagnostic in diagnostics:
    diagnosticBytes = split(diagnostic)
    index = 0
    for diagnosticByte in diagnosticBytes:
        bytes[index][int(diagnosticByte)] += 1
        index += 1

gamma = ""
epsilon = ""
for byte in bytes:
    gamma += str(max(bytes[byte], key=bytes[byte].get) )
    epsilon += str(min(bytes[byte], key=bytes[byte].get) )

gammaRate = int(gamma, 2)
epsilonRate = int(epsilon, 2)

powerConsumption = gammaRate * epsilonRate

print(powerConsumption)
