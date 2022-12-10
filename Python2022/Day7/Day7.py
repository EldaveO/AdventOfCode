# input file
data = open("Day7\Sample.txt").readlines()
#data = open("Day7\Data.txt").readlines()
data = [line.strip() for line in data]

def commandCheck(line, lineNumber):
    commandCharater = "$"
    commandGoMain = "cd /"
    commandGoBack = "cd .."
    commandGoInto = "cd"
    commandListAll = "ls"
    if any(c in commandCharater for c in line):
        if commandGoMain in line:
            return "goMain", lineNumber
        elif commandGoBack in line:
            return "goBack", lineNumber
        elif commandGoInto in line:
            return "goInto", lineNumber
        elif commandListAll in line:
            return "listAll", lineNumber
        else:
            return "commandNotFound", lineNumber
    else: 
        return "file", lineNumber

def goMain():
    pass

def goBack(currentDirectory, newDirectory):
    return newDirectory

def goInto(lineNumber, line):
    return None

def listAll(data, directory, lineNumberStart, LineNumberEnd):
    lines = []
    for i, line in enumerate(data):
        if i in lineNumber:
            lines.Append(line.strip()) 
    return lines

def part1(data):
    i = int(0)
    currentDirectory = "/"
    previousDirectories = []
    lines = []

    for line in data:
        i += 1
        currentCommand, lineNumber = commandCheck(line, i)
        
        if currentCommand == "goMain":
            previousDirectories.clear()
            previousDirectories.append("/")
            currentDirectory = "/"
        elif currentCommand == "goBack":
            return goBack()
        elif currentCommand == "goInto":
            previousDirectories.append()
            return goInto()
        elif currentCommand == "listAll":
            lines.clear()
            for line in data:
                commandCheck(line)
            for line in data: 
            return listAll()


    return data

def part2(data):
    return None    
           
part1(data)
#print(part2(data))