# input file
data = open("Day4\Sample.txt").readlines()
#data = open("Day4\Data.txt").readlines()
data = [line.strip() for line in data]
#print(data)

def part1(data):
    for line in data:
        