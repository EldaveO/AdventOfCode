# input file
#data = open("Day3\Sample.txt").readlines()
data = open("Day3\Data.txt").readlines()
#data = open("Day3\Sample2.txt").readlines()
data = [line.strip() for line in data]
#print(data)


def part1(data):
    prioritySum = int(0)
    for line in data:
        firstSack = line[:len(line)//2]
        secondSack = line[len(line)//2:]
        a = list(set(firstSack) & set(secondSack))
        for i in a:
            i = ord(i)
            if i > 96:
                prioritySum += i-96
            else:
                prioritySum += i-38
    return prioritySum


def part2(data):
    prioritySum = int(0)
    j = int(0)
    while len(data) > 1:
        thirdElf = data.pop(2)
        secondElf = data.pop(1)
        firstElf = data.pop(0)
        a = list(set(firstElf) & set(secondElf) & set(thirdElf))
        for i in a:
            print(i)
            i = ord(i)
            print(i)
            if i > 96:
                prioritySum += i-96
            else:
                prioritySum += i-38
            print("current total: "+ str(prioritySum)) 
        j += 1
    print("rounds went: " + str(j))           
    return prioritySum


#print(part1(data))
print(part2(data))