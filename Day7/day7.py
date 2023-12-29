def openFile():
    #Locate and read the file
    filename = "RaceData.txt"
    #filename = "RaceSample.txt"
    return open(filename, "r")

File = openFile()
for count, line in enumerate(File):
    pass