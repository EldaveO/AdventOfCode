# input file
#data = open("Day5\Sample.txt").readlines()
moveList = open("Day5\SampleMoveList.txt").readlines()
cargoStacks = open("Day5\SampleCargoStacks.txt").readlines()
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
    for move in moveList:
        amountMove = int(moveList[i][0])
        startMove = int(moveList[i][1])+1
        endMove = int(moveList[i][2])-1

        j = int(0)
        while j <= 1: #int(amountMove):
            cargoCrate = cargoStacks[startMove][-1]
            cargoStacks[startMove].pop([startMove][-1])
            cargoStacks[endMove].append(cargoCrate)
            print(cargoCrate)
            print(cargoStacks)
            j =+ 1
        i += 1

    return None

part1(cargoStacksFix(cargoStacks), moveListFix(moveList))         
#(part1(data))
#print(part2(data))