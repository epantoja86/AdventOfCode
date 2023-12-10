def openFile():
    #Locate and read the file
    filepath = "/Users/eddie.pantoja.cache/CodeBase/AdventofCode/Day5/"
    #filename = "SeedMap.txt"
    filename = "SeedSample.txt"
    return open(filepath + filename, "r")

def CreateMap():
    return "Map"

File = openFile()
for card, line in enumerate(File):
    pass
SoilMap = CreateMap()
FertMap = CreateMap()
WaterMap = CreateMap()
LightMap = CreateMap()
TempMap = CreateMap()
HumidMap = CreateMap()
LocMap = CreateMap()
