import copy
filename = 'input/day3.txt'
with open(filename) as file:
    lines = file.readlines()
    diagnostics = [line.rstrip() for line in lines]

def stripDiagnostics(list, bytes, type):
    index = 0
    for postion in range(len(list)):
        if len(list) != 1:
            for item in list:
                itemBit = item[index]
                bytes[index][int(itemBit)] += 1
            
            compare = min(bytes[postion], key=bytes[postion].get)
            if(type == "oxygen"):
                compare = max(bytes[postion], key=bytes[postion].get)
            if (bytes[postion][0] == bytes[postion][1]) : 
                compare = 1 if type == "oxygen" else 0  
                
            list = [i for i in list if i[index] == str(compare)]
            index += 1
        else :
            value = int(list[0], 2)
    return value

bytes = {}
for i in range(len(diagnostics[0])) :
    bytes[i] = {0:0, 1:0}

bytesOxygen = copy.deepcopy(bytes)
bytesCO2 = copy.deepcopy(bytes)

oxygen = stripDiagnostics(diagnostics, bytesOxygen, "oxygen")
CO2 = stripDiagnostics(diagnostics, bytesCO2,  "CO2")

print(oxygen * CO2)
