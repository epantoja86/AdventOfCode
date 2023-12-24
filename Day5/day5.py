def openFile():
    #Locate and read the file
    filename = "SeedMap.txt"
    #filename = "SeedSample.txt"
    return open(filename, "r")

#Initialise Lists
seeds = []
seedrange = []
soil = []
fert = []
water = []
light = []
temp = []
humid = []
loc = []
headings = [
    "seeds:",
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location"
    ]

def part1():
    locations = []
    heading = ""
    File = openFile()
    for count, line in enumerate(File):
        x = line.split()
        if len(x) > 0:
            if heading == "seed":
                soil.append(x)
            elif heading == "soil":
                fert.append(x)
            elif heading == "fert":
                water.append(x)
            elif heading == "water":
                light.append(x)
            elif heading == "light":
                temp.append(x)
            elif heading == "temp":
                humid.append(x)
            elif heading == "humid":
                loc.append(x)
        else:
            heading = ""
        for x in headings:
            if not line.find(x) == -1:
                if x == "seeds:":
                    seeds = line.split()
                    seeds.remove("seeds:")
                    break
                else:
                    if x == "seed-to-soil":
                        heading = "seed"
                    elif x == "soil-to-fertilizer":
                        heading = "soil"
                    elif x == "fertilizer-to-water":
                        heading = "fert"
                    elif x == "water-to-light":
                        heading = "water"
                    elif x == "light-to-temperature":
                        heading = "light"
                    elif x == "temperature-to-humidity":
                        heading = "temp"
                    elif x == "humidity-to-location":
                        heading = "humid"
                    break
    File.close
    for x in seeds:
        value = int(x)
        for y in soil:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in fert:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in water:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in light:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in temp:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in humid:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in loc:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        locations.append(value)
    locations.sort()
    return locations[0]

def part2():
    locations = []
    heading = ""
    File = openFile()
    for count, line in enumerate(File):
        x = line.split()
        if len(x) > 0:
            if heading == "seed":
                soil.append(x)
            elif heading == "soil":
                fert.append(x)
            elif heading == "fert":
                water.append(x)
            elif heading == "water":
                light.append(x)
            elif heading == "light":
                temp.append(x)
            elif heading == "temp":
                humid.append(x)
            elif heading == "humid":
                loc.append(x)
        else:
            heading = ""
        for x in headings:
            if not line.find(x) == -1:
                if x == "seeds:":
                    seeds = line.split()
                    seeds.remove("seeds:")
                    for y in range(len(seeds)):
                        if (y % 2) == 0:
                            for z in range(int(seeds[y+1])):
                                seedrange.append(z + int(seeds[y]))
                    break
                else:
                    if x == "seed-to-soil":
                        heading = "seed"
                    elif x == "soil-to-fertilizer":
                        heading = "soil"
                    elif x == "fertilizer-to-water":
                        heading = "fert"
                    elif x == "water-to-light":
                        heading = "water"
                    elif x == "light-to-temperature":
                        heading = "light"
                    elif x == "temperature-to-humidity":
                        heading = "temp"
                    elif x == "humidity-to-location":
                        heading = "humid"
                    break
    File.close
    for x in seedrange:
        value = int(x)
        for y in soil:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in fert:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in water:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in light:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in temp:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in humid:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        for y in loc:
            if value >= int(y[1]) and value < (int(y[1])+int(y[2])):
                value = value + int(y[0])-int(y[1])
                break
        locations.append(value)
    locations.sort()
    return locations[0]

#print("Closest location (single): " + str(part1()))
print("Closest location: (range): " + str(part2()))
