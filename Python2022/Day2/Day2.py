# input file
#data = open("Day2\Sample.txt").readlines()
data = open("Day2\Data.txt").readlines()
data = [line.strip() for line in data]
print(data)

def part1(data):
    pointCount = int(0)
    rockPoint = int(1)
    paperPoint = int(2)
    scissorPoint = int(3)
    winPoint = int(6)
    drawPoint = int(3)
    losePoint = int(0)

    for line in data:
        opponent, me = line.split(" ")
        #add selection point
        if me == "X":
            pointCount += rockPoint
            me = "rock"
        elif me == "Y":
            pointCount += paperPoint
            me = "paper"
        elif me == "Z":
            pointCount += scissorPoint
            me = "scissor"
        #add match point
        if opponent == "A" and me == "rock":
            pointCount += drawPoint
        elif opponent == "A" and me == "paper":
            pointCount += winPoint
        elif opponent == "A" and me == "scissor":
            pointCount += losePoint
        elif opponent == "B" and me == "rock":
            pointCount += losePoint
        elif opponent == "B" and me == "paper":
            pointCount += drawPoint
        elif opponent == "B" and me == "scissor":
            pointCount += winPoint
        elif opponent == "C" and me == "rock":
            pointCount += winPoint
        elif opponent == "C" and me == "paper":
            pointCount += losePoint
        elif opponent == "C" and me == "scissor":
            pointCount += drawPoint                                     
    return pointCount

def part2(data):
    pointCount = int(0)
    rockPoint = int(1)
    paperPoint = int(2)
    scissorPoint = int(3)
    winPoint = int(6)
    drawPoint = int(3)
    losePoint = int(0)

    for line in data:
        opponent, me = line.split(" ")
        #add selection point
        if me == "X":
            pointCount += losePoint
        elif me == "Y":
            pointCount += drawPoint
        elif me == "Z":
            pointCount += winPoint
        #add match point
        if opponent == "A" and me == "X":
            pointCount += scissorPoint
        elif opponent == "A" and me == "Y":
            pointCount += rockPoint
        elif opponent == "A" and me == "Z":
            pointCount += paperPoint
        elif opponent == "B" and me == "X":
            pointCount += rockPoint
        elif opponent == "B" and me == "Y":
            pointCount += paperPoint
        elif opponent == "B" and me == "Z":
            pointCount += scissorPoint
        elif opponent == "C" and me == "X":
            pointCount += paperPoint
        elif opponent == "C" and me == "Y":
            pointCount += scissorPoint
        elif opponent == "C" and me == "Z":
            pointCount += rockPoint                                     
    return pointCount

print(part1(data))
print(part2(data))