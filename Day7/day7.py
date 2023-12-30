cardLabels = [
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2"
    ]

def openFile():
    #Locate and read the file
    #filename = "CardHands.txt"
    filename = "CardSample.txt"
    return open(filename, "r")

def collectHands():
    File = openFile()
    Hands =[]
    for count, line in enumerate(File):
        x = line.split()
        Hands.append([x[0],x[1]])
    File.close
    return Hands

def sortHands(toSort):
    fivekindList = [x for x in toSort if fivekind(x[0])]
    fourkindList = [x for x in toSort if fourkind(x[0])]
    fullhouseList = [x for x in toSort if fullhouse(x[0])]
    threekindList = [x for x in toSort if threekind(x[0])]
    twopairList = [x for x in toSort if twopair(x[0])]
    pairList = [x for x in toSort if pair(x[0])]
    highCardList = [x for x in toSort if highCard(x[0])]
    
    for a in fivekindList:
        

    return fivekindList + fourkindList + fullhouseList + threekindList + twopairList + pairList + highCardList

def fivekind(value):
    for c in cardLabels:
        if value.count(c) == 5:
            return True
    return False

def fourkind(value):
    for c in cardLabels:
        if value.count(c) == 4:
            return True
    return False

def fullhouse(value):
    for c in cardLabels:
        if value.count(c) == 3:
            if pair(value.replace(c,"")):
                return True
    return False

def threekind(value):
    for c in cardLabels:
        if value.count(c) == 3:
            if pair(value.replace(c,"")):
                return False
            return True
    return False

def twopair(value):
    for c in cardLabels:
        if value.count(c) == 2:
            if pair(value.replace(c,"")):
                return True
    return False

def pair(value):
    for c in cardLabels:
        if value.count(c) == 2:
            if threekind(value.replace(c,"")):
                return False
            if pair(value.replace(c,"")):
                return False
            return True
    return False

def highCard(value):
    if fivekind(value):
        return False
    elif fourkind(value):
        return False
    elif fullhouse(value):
        return False
    elif threekind(value):
        return False
    elif twopair(value):
        return False
    elif pair(value):
        return False
    return True

print(sortHands(collectHands()))
