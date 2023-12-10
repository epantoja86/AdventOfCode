special_characters ="!@#$%^&*()-+?_=,<>/"

def openFile():
    #Locate and read the file
    filepath = "/Users/eddie.pantoja.cache/CodeBase/AdventofCode/Day4/"
    #filename = "ScratchSample.txt"
    filename = "ScratchCards.txt"
    return open(filepath + filename, "r")

def readString(string):
    List = []
    number = ""
    for x in string:
        if x.isnumeric():
            number = number + x
        elif len(number) > 0:
            List.append(number)
            number = ""
    return List

def findMatches(list1,list2):
    return len(list(set(list1) & set(list2)))

def part1(f):
    result = 0
    for count, line in enumerate(f):
        ListLeft = readString(line[line.find(":")+1:line.find("|")-1] + " ")
        ListRight = readString(line[line.find("|")+1:] + " ")
        x = len(list(set(ListLeft) & set(ListRight)))
        if x > 0:
            result = result + 2**(x-1)
    return result

def part2(f):
    rewards = []
    result = []
    for card, line in enumerate(f):
        ListLeft = readString(line[line.find(":")+1:line.find("|")-1] + " ")
        ListRight = readString(line[line.find("|")+1:] + " ")
        rewards.append(findMatches(ListLeft,ListRight))
    for card in range(len(rewards)):
        result.append(1)
    for row in range(len(result)):
        for cards in range(result[row]):
            for copy in range(rewards[row]):
                y = row + copy +1
                result[y] = result[y]+1
    return sum(result)

File = openFile()
print ("Total of " + str(part1(File)) + " Points")
File = openFile()
print (str(part2(File)) + " Scratch cards in total")