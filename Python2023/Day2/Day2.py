# input file
#data = open("Day2\Sample.txt").readlines()
data = open("Day2\Data.txt").readlines()
data = [line.strip() for line in data]
#print(data)

def part1(data):
    redCubeTotal = 12
    greenCubeTotal = 13
    blueCubeTotal = 14
    successTotal = 0
    lineNumber = 0
    
    for line in data:
        gameNumber = line.split("Game ")
        gameNumber, pullData = gameNumber[1].split(": ")
        lineNumber += 1
        print(lineNumber)

        
        pullData = pullData.split("; ")
        
        pullCheck = True
        for pull in pullData:
            pull = pull.split(", ")

            for grab in pull:                
                number, colour = grab.split(" ")
                number = int(number)
                if colour == "red" and number > redCubeTotal:
                    print("bad Pull: ", colour, number)
                    pullCheck = False
                elif colour == "green" and number > greenCubeTotal:
                    print("bad Pull: ", colour, number)
                    pullCheck = False
                elif colour == "blue" and number > blueCubeTotal:
                    print("bad Pull: ", colour, number)
                    pullCheck = False
        
        if pullCheck == True:
            print("Good Game:", lineNumber)
            successTotal += lineNumber  
        else:
            print("Bad Game:", lineNumber)
            
    return successTotal

print('Success total: ', part1(data))