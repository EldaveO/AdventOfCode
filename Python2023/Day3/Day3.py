# input file
data = open("Day3\Sample.txt").readlines()
#data = open("Day3\Data.txt").readlines()
data = [line.strip() for line in data]

def isValidCoordinate(i, j, rows, cols):
    return 0 <= i < rows and 0 <= j < cols

def part1(data):
    rows = len(data)
    cols = len(data[0])
    
    symbols = set(['.','*','#','+','$','@','=','/','%','&','=','-'])
    
    totalSum = 0
    
    return totalSum
      
print(part1(data))