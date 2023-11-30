# input file
data = open("Day4\Sample.txt").readlines()
#data = open("Day4\Data.txt").readlines()
data = [line.strip() for line in data]
#print(data)


def part1(data):
    thingCounter = int(0)
    for line in data:
        elfOne, elfTwo = line.split(",")
        elfOneMin, elfOneMax = elfOne.split("-")
        elfTwoMin, elfTwoMax = elfTwo.split("-")
        elfOneList, elfTwoList = [], []
        elfMax = max(int(elfOneMax), int(elfTwoMax))

        #fill List with values
        for x in range(int(elfMax)+1):
            elfOneList.insert(x, 1)
            elfTwoList.insert(x, 2)
        for x in range(int(elfOneMin), int(elfOneMax)+1):
            elfOneList[x] = 3
        for x in range(int(elfTwoMin), int(elfTwoMax)+1):
            elfTwoList[x] = 3

        #compare the two lists

        matchCount = int(0)
        matchMin = min(elfOneList.count(3) , elfTwoList.count(3))   
        for i in range(len(elfOneList)):
            #print(x)
            if elfOneList[i] == elfTwoList[i]:
                matchCount += 1
        if matchCount == matchMin and matchMin > 0:
            print("elf1:" + str(elfOneList))
            print("elf2:" + str(elfTwoList))
            print("match")
            thingCounter += 1        
    return thingCounter

def part2(data):
    thingCounter = int(0)
    for line in data:
        elfOne, elfTwo = line.split(",")
        elfOneMin, elfOneMax = elfOne.split("-")
        elfTwoMin, elfTwoMax = elfTwo.split("-")
        elfOneList, elfTwoList = [], []
        elfMax = max(int(elfOneMax), int(elfTwoMax))

        #fill List with values
        for x in range(int(elfMax)+1):
            elfOneList.insert(x, 1)
            elfTwoList.insert(x, 2)
        for x in range(int(elfOneMin), int(elfOneMax)+1):
            elfOneList[x] = 3
        for x in range(int(elfTwoMin), int(elfTwoMax)+1):
            elfTwoList[x] = 3

        #compare the two lists

        matchCount = int(0)
        matchMin = min(elfOneList.count(3) , elfTwoList.count(3))   
        for i in range(len(elfOneList)):
            #print(x)
            if elfOneList[i] == elfTwoList[i]:
                matchCount = 1
        if matchCount == 1 and matchMin > 0:
            print("elf1:" + str(elfOneList))
            print("elf2:" + str(elfTwoList))
            print("match")
            thingCounter += 1        
    return thingCounter    
           
print(part1(data))
print(part2(data))