day4 = open("Day4\Sample.txt").readlines()
#day4 = open("Day4\data.txt").readlines()
day4 = [line.strip() for line in day4]

def part1(data):
    for line in data:
        thing = line.split("\n")
        print(thing)


part1(day4)