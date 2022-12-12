# input file
#data = open("Day7\Sample.txt").readlines()
data = open("Day7\Data.txt").readlines()
data = [line.strip() for line in data]

def commandCheck(line):
    commandCharater = "$"
    commandGoMain = "cd /"
    commandGoBack = "cd .."
    commandGoInto = "cd"
    commandListAll = "ls"
    if any(c in commandCharater for c in line):
        if commandGoMain in line:
            return "goMain"
        elif commandGoBack in line:
            return "goBack"
        elif commandGoInto in line:
            return "goInto" 
        elif commandListAll in line:
            return "listAll"
        else:
            return "commandNotFound"
    else: 
        return "file"

def part1(data):
    currentDirectory = []
    directoryList = {}
    totalSum = int(0)

    for line in data:
        currentCommand = commandCheck(line)        
        if currentCommand == "goMain":
            currentDirectory.clear()
            currentDirectory.append("/")
        elif currentCommand == "goBack":
            currentDirectory.pop()
        elif currentCommand == "goInto":
            dollar, cd, folder = line.split(" ")
            currentDirectory.append(folder)
            #print(currentDirectory)
        elif currentCommand == "listAll":
            pass
        else: #is a file or a dir
            #parse the file/dir and split at the space
            number, fileName = line.split(" ")
            #check if string or int
            if number == "dir":
                pass
            else:
                locationName = "/".join(currentDirectory)
                #print("/".join(poop))
                if directoryList.get(locationName) is not None:
                    currentTotal = int(directoryList.get(locationName))
                    currentTotal += int(number)
                    #directoryList.update({locationName: currentTotal})
                    directoryList[locationName] = currentTotal
                else:
                    #directoryList.update({locationName: int(number)})
                    directoryList[locationName] = int(number)
    for key in directoryList:
        if int(directoryList[key]) <= 100000:
            totalSum += int(directoryList[key])    
    return totalSum

def part2(data):
    return None    
           
print(part1(data))
#print(part2(data))