#day3 = open("Day3\Sample.txt").readlines()
day3 = open("Day3\data.txt").readlines()
day3 = [line.strip() for line in day3]


def part1(data):
    treeCount = int(0)
    x = int(0)  # string array holder (Horizontal position)
    y = int(1)  # index in the list (Vertical position)
    print(list(data[0]))
    for line in data:
        #print(y)
        if y >= len(data):
            return treeCount
        else:
            currentRow = list(data[y])    
            # Movement check
            #Shmebulock — Today at 6:04 PM
            #x = (x + 1) % len(date[0])` 
            #Lally Monkey — Today at 6:09 PM
            #x += 3
            #if x >= len(data[0]):
                #x = x - len(data[0])
            if (x + 3) >= len(data[0]):
                x = (x + 3) - (len(data[0]))
                #print(x)
            else:
                x += 3
                #print(x)
            # Tree Check
            if currentRow[x] == "#":
                treeCount += 1
                currentRow[x] = "X"
                print(currentRow)
                #print(data[y] + " Row:" + str(y) +" Hit!")
            else:         
                #print(data[y] + " Row:" + str(y) +" Miss!")
                currentRow[x] = "O"
                print(currentRow)
            y += 1    

def part2(data, right, down):
    treeCount = int(0)
    x = int(0)  # string array holder (Horizontal position)
    y = int(down)  # index in the list (Vertical position)
    print(list(data[0]))
    for line in data:
        #print(y)
        if y >= len(data):
            return treeCount
        else:
            currentRow = list(data[y])    
            # Movement check
            if (x + right) >= len(data[0]):
                x = (x + right) - (len(data[0]))
                #print(x)
            else:
                x += right
                #print(x)
            # Tree Check
            if currentRow[x] == "#":
                treeCount += 1
                currentRow[x] = "X"
                print(currentRow)
                #print(data[y] + " Row:" + str(y) +" Hit!")
            else:         
                #print(data[y] + " Row:" + str(y) +" Miss!")
                currentRow[x] = "O"
                print(currentRow)
            y += down    
  
print("check1")
value1 = part2(day3, 1, 1)
print("check2")
value2 = part2(day3, 3, 1)
print("check3")
value3 = part2(day3, 5, 1)
print("check4")
value4 = part2(day3, 7, 1)
print("check5")
value5 = part2(day3, 1, 2)

value = value1 * value2 * value3 * value4 * value5

print("trees Hit: " + str(value))
# print(day3)
