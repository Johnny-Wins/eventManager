def main(): 

    memory = open("eventMemory.txt")

    memoryData = []

    for line in memory:
        memoryData.append(line)

    evenNums = range(0,len(memoryData),2)
    oddNums = range(1,len(memoryData),2)

    for x in evenNums:
        print(x)

    for x in oddNums:
        print(x)

main()