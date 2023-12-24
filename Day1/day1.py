numbers = {
        "one" : "o1e",
        "two" : "t2o",
        "three" : "th3ee",
        "four" : "fo4r",
        "five" : "fi5e",
        "six" : "s6x",
        "seven" : "se7en",
        "eight" : "ei8ht",
        "nine" : "nin9e"
    }

def part1(text):
    n = []
    for x in text:
        if x.isnumeric():
            n.append(x)
    return int(n[0] + n[-1])

def part2(text):
    for key,value in numbers.items():
        text = (text.replace(key,str(value)))
    return text

#Locate and read the file
filename = "CalibrationInput.txt"
#filename = "inputtest.txt"
f = open(filename, "r")

#Initialise variables
sum = 0
#Process line by line
for count, line in enumerate(f):
    #Translate the spelt numbers
    #print (count+1)
    fixedLine = part2(line)
    #Return calibration value
    sum = sum + part1(fixedLine)
print('The calibration number is ', sum)
f.close