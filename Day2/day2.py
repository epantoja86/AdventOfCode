from functools import reduce

config = {
    "red" : 12,
    "green" : 13,
    "blue" :14
}

#Locate and read the file
filename = "InputRecord.txt"
#filename = "TestRecord.txt"
f = open(filename, "r")

def part1(text):
    for key,value in config.items():
        start = 0
        for x in range(text.count(key)):
            start = line.find(key,start)+1
            if config[key] < int(line[(start-4):start-1]):
                return False
    return True

def part2(text):
    n = []
    for key,value in config.items():
        n.append(0)
        start = 0
        for x in range(text.count(key)):
            start = text.find(key,start)+1
            y = int(text[(start-4):start-1])
            if n[-1] < y:
                n.pop()
                n.append(int(y))
    return reduce(lambda x, y: x*y, n)

sum = 0
power = 0
for gameID, line in enumerate(f):
    if part1(line) == True:
        sum = sum + gameID + 1
    power = power + part2(line)
print('The sum of all valid gameIDs are ', sum)
print('The sum of the power of cubes are ', power)