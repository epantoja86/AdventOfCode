def openFile():
    #Locate and read the file
    #filename = "SeedMap.txt"
    filename = "SeedSample.txt"
    return open(filename, "r")

def CreateMap():
    return "Map"

#Initialise Dictionaries
soil = []
fert = []
water = []
light = []
temp = []
humid = []
loc = []

File = openFile()
for count, line in enumerate(File):
    print("Reading line " + str(count+1))
SoilMap = CreateMap()
FertMap = CreateMap()
WaterMap = CreateMap()
LightMap = CreateMap()
TempMap = CreateMap()
HumidMap = CreateMap()
LocMap = CreateMap()
