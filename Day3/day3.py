special_characters ="!@#$%^&*()-+?_=,<>/"

def openFile():
    #Locate and read the file
    #filename = "SampleSchematic.txt"
    filename = "EngineSchematic.txt"
    return open(filename, "r")

def createArray(file):
    #Create Array
    n = []
    for count, line in enumerate(file):
        list = []
        for x in line:
            list.append(x)
        list.insert(0,".")
        list.pop()
        list.append(".")
        n.append(list)
    return n

def createMargin(n, width):
    #Create Margin
    list = []
    for count in range(width):
        list.append(".")
    n.insert(0,list)
    n.append(list)
    return n

def part1(n,searchItems):
    number = ""
    list = []
    for row in range(len(n)):
        for col in range(len(n[row])):
            x = (n[row][col])
            if not x.isnumeric():
                if len(number) > 0:
                    for horiz in range(len(number)+2):
                        for vert in range(3):
                            y = n[row+1-vert][col-horiz]
                            if any(c in searchItems for c in y):
                                list.append(int(number))
                number = ""
            else:
                number = number + x
    return list

def part2(n):
    list = []
    result = 0
    for row in range(len(n)):
        for col in range(len(n[row])):
            x = (n[row][col])
            if any(c in "*" for c in x):
                n[row][col] = "H"
                Snippet = n[row-1:row+2]
                Snippet.insert(0,n[0])
                Snippet.append(n[-1])
                list = part1(Snippet,"H")
                if  len(list) == 2:
                    result = result + list[0] * list[1]
                n[row][col] = "*"
    return result
File = openFile()
Array = createArray(File)
Array = createMargin(Array, len(Array[0]))
print("Part Numbers: " + str(sum(part1(Array,special_characters))))
print("Gear Ratios: " + str(part2(Array)))