# input file
#data = open("Day6\Sample3.txt").readline()
data = open("Day6\Data.txt").readline()

def part1(data):
    data = list(data)
    i = int(0)
    j = int(4)
    for char in data:
        code = data[i:j]
        for letter in code:
            if code[0] == code[1] or code[0] == code[2] or code[0] == code[3]:
                print("nope")
            elif code[1] == code[2] or code[1] == code[3]:
                print("nope")
            elif code[2] == code[3]:
                print("nope")
            else:
                print(code)
                return j     
        i += 1
        j += 1             

    #print(code) 
    return None

def part2(data):
    data = list(data)
    i = int(0)
    j = int(14)
    for char in data:
        code = data[i:j]
        setCode = set(code)
        if(len(code) == len(setCode)):
            print(code)
            return j            
        i += 1
        j += 1             

    #print(code) 
    return None    
           
#print(part1(data))
print(part2(data))