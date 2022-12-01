# input file
#data = open("Day1\Sample.txt").readlines()
#data = open("Day1\Sample2.txt").readlines()
data = open("Day1\Data.txt").readlines()
data = [line.strip() for line in data]
#print(data)

def part1(data):
    mostCalories = int(0)
    currentSum = int(0)
    for line in data:
        if (line != ''):
            currentSum += int(line)
            #print(currentSum)
        else:
            if (mostCalories <= currentSum):
                mostCalories = currentSum
            currentSum = 0    
    if (mostCalories <= currentSum):
                mostCalories = currentSum
    return mostCalories    

def part2(data):
    currentSum = int(0)
    values = []
    for line in data:
        if (line != ''):
            currentSum += int(line)
        else:
            values.append(currentSum)  
            currentSum = 0
            #print(values)
    #Thanks Dr James!
    collection = values[:]
    for j in range(len(collection)):
        for i in range(len(collection) - 1 - j):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]

    firstMost = collection[(len(collection))-1]
    secondMost = collection[(len(collection))-2]
    thirdMost = collection[(len(collection))-3]
    total = firstMost + secondMost + thirdMost

    return total

print(part2(data))