#f = open("Day2\Sample.txt", "r")
#day2 = open("Day2\Sample.txt").readlines()
day2 = open("Day2\data.csv").readlines()
day2 = [line.strip() for line in day2]

def part1(day2):
    count = int(0)
    for line in day2:
        key, value = line.split(": ")
        v1, v2 = key.split(" ")[0].split("-")
        v = key.split(" ")[1]
        if int(v1) <= value.count(v) <= int(v2):
            count = count+1
    return count

def part2(day2):
    passwordList = []
    count = int(0)
    for line in day2:
        key, value = line.split(": ")
        v1, v2 = key.split(" ")[0].split("-")
        v = key.split(" ")[1]
        passwordList.append([v1, v2, v, value])
        if (v == value[int(v1)-1] and v != value[int(v2) - 1]) or (v == value[int(v2)-1] and v != value[int(v1) - 1]):
            count += 1
    print(passwordList)
    print(passwordList[0][3][0])        
    return count

value = part2(day2)
print(value)