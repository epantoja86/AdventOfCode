def openFile():
    #Locate and read the file
    filename = "RaceData.txt"
    #filename = "RaceSample.txt"
    return open(filename, "r")

def part1():
    File = openFile()
    for count, line in enumerate(File):
        x = line.split()
        if x[0] == "Time:":
            times = x
            times.pop(0)
        else:
            distances = x
            distances.pop(0)
    File.close
    results = []
    for x in range(len(times)):
        y = [times[x],distances[x]]
        results.append(y)
    return results

def part2():
    File = openFile()
    for count, line in enumerate(File):
        x = line.replace(" ","")
        if x.find("Time"):
            distance = x[9:]
        else:
            time= x[5:-1]
    File.close
    return [[time,distance],]

def ProcessData(RaceData):
    prod_of_options = 1
    for x in RaceData:
        options = 0
        for time_button_push in range(int(x[0])):
            total_time = int(x[0])
            current_record = int(x[1])
            time_remaining = total_time - time_button_push
            speed = time_button_push
            distance_travelled = speed * time_remaining
            if distance_travelled > current_record:
                options = options + 1
        prod_of_options = prod_of_options * options
    return prod_of_options

print("Product of options: " + str(ProcessData(part1())))
print("Options in single race: " + str(ProcessData(part2())))