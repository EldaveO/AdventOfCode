import time
# input file
#data = open("Day4\Sample.txt").readlines()
data = open("Day4\Data.txt").readlines()
data = [line.strip() for line in data]
#print(data)

def part1(data):
    score = 0
    for line in data:
        line = line.replace("  ", " ")
        line = line.split(": ")
        ticket = line[1].split(" | ")
        winningNumbers = ticket[0].split(" ")        
        ticketNumbers = ticket[1].split(" ")
        x = -1
        for number in ticketNumbers:
            if number in winningNumbers:
                x += 1
                #print("winner: ", number)
        if x >= 0:
            score += (2**x)
        #print("point total: ", score)   
    return score

def part2(data):
    cardCopies = []
    for line in data:
        cardCopies.append(1)
    
    for line in data:
        line = line.replace("  ", " ")
        line = line.split(": ")
        currentTicketNumber = (int(line[0].strip("Card "))-1)
        ticket = line[1].split(" | ")
        winningNumbers = ticket[0].split(" ")        
        ticketNumbers = ticket[1].split(" ")
        i = 1
        for i in range(cardCopies[currentTicketNumber]):
            x = int(currentTicketNumber)+1
            for number in ticketNumbers:
                if number in winningNumbers:    
                    cardCopies[x] += 1
                    x += 1
            i += 1     
    return sum(cardCopies)        

start = time.time()
print("Part 1: ", part1(data))
print("Part 2: ", part2(data))
end = time.time()
print("This took: ", (end - start), " seconds to run!")