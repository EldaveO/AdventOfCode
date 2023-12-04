# input file
data = open("Sample.txt").readlines()
#data = open("Data.txt").readlines()
#data = [line.strip() for line in data]
#print(data)

def part1(data):
    calibrationTotal = 0
    for line in data:
           firstDigit = next(char for char in line if char.isdigit())
           lastDigit = next(char for char in reversed(line) if char.isdigit())
           calibrationValue = int(firstDigit + lastDigit)
           calibrationTotal += calibrationValue
    return calibrationTotal

def part2(data):    
    for line in data:
        print("poop")
    return "done"
      
#print(part1(data))
print(part2(data))

