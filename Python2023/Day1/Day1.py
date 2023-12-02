import re
# input file
#data = open("Day1\Sample.txt").readlines()
#data = open("Day1\Sample2.txt").readlines()
data = open("Data.txt").readlines()
data = [line.strip() for line in data]
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
    calibrationTotal = 0
    for line in data:
           digits = re.findall(r'\b(one|two|three|four|five|six|seven|eight|nine)\b|\d', line)
           firstDigit = digits[0] if digits[0].isdigit() else str(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(digits[0]) + 1)
           lastDigit = digits[-1] if digits[-1].isdigit() else str(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(digits[-1]) + 1)
           calibrationValue = int(firstDigit + lastDigit)
           calibrationTotal += calibrationValue
    return calibrationTotal

print(part1(data))
print(part2(data))