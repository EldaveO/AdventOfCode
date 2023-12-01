# input file
#data = open("Day1\Sample.txt").readlines()
#data = open("Day1\Sample2.txt").readlines()
data = open("Day1\Sample.txt").readlines()
data = [line.strip() for line in data]
#print(data)

def part1(data):
    firstDigit = int(11)
    secondDigit = int(22)
    Sums = list()
    for line in data:
           for char in line:
                if firstDigit == 11 and char.isdigit(): 
                    firstDigit = char
                elif secondDigit == 22 and char.isdigit():
                    secondDigit = char
                elif firstDigit != 11 and secondDigit != 22:
                    

        return

print(part1(data))