# input file
#data = open("Day5\Sample.txt").readlines()
#moveList = open("Day5\SampleMoveList.txt").readlines()
#cargoStacks = open("Day5\SampleCargoStacks.txt").readlines()
moveList = open("Day5\MoveList.txt").readlines()
cargoStacks = open("Day5\CargoStacks.txt").readlines()
#data = open("Day5\Data.txt").readlines()

def moveListFix(moveList):
    moveList = [line.strip() for line in moveList]
    moveList = [line.replace("move ", "") for line in moveList]
    moveList = [line.replace(" from ", ",") for line in moveList]
    moveList = [line.replace(" to ", ",") for line in moveList]
    moveList = [line.split(",") for line in moveList] 
    return moveList

def cargoStacksFix(cargoStacks):
    cargoStacks = [line.strip() for line in cargoStacks]
    cargoStacks = [line.split(" ") for line in cargoStacks]
    return cargoStacks

def part1(cargoStacks, moveList):
    i = int(0)
    topStack = []
    for move in moveList:
        amountMove = int(moveList[i][0])
        startMove = int(moveList[i][1])-1
        endMove = int(moveList[i][2])-1

        j = int(0)
        while j < amountMove:
            cargoCrate = cargoStacks[startMove][-1]
            cargoStacks[startMove].pop()
            cargoStacks[endMove].append(cargoCrate)
            #print(cargoCrate)
            #print(cargoStacks)
            j += 1
        i += 1

    i = int(0)    
    for stack in cargoStacks:
        topStack.append(cargoStacks[i][-1])
        i += 1
    #print(topStack)    
    return topStack

def part2(cargoStacks, moveList):
    i = int(0)
    topStack = []
    cargoCrate = []
    for move in moveList:
        amountMove = int(moveList[i][0])
        startMove = int(moveList[i][1])-1
        endMove = int(moveList[i][2])-1

        j = int(0)
        while j < amountMove:
            cargoCrate.append(cargoStacks[startMove][-1])
            cargoStacks[startMove].pop()
            
            j += 1
        cargoCrate.reverse()
        k = int(0)
        for cargo in cargoCrate:   
            cargoStacks[endMove].append(cargoCrate[k])
            k += 1
        cargoCrate.clear() 
        #print(cargoStacks)
        i += 1

    i = int(0)    
    for stack in cargoStacks:
        topStack.append(cargoStacks[i][-1])
        i += 1
    #print(topStack)    
    return topStack    

print(part1(cargoStacksFix(cargoStacks), moveListFix(moveList)))         
print(part2(cargoStacksFix(cargoStacks), moveListFix(moveList)))    