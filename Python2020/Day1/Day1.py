# input file
f = open("Day1\Day1Data.csv", "r")
#f = open("Day1\Day1Sample.csv", "r")

a = f.read().split("\n")
b = []
for i in a:
    b.append(int(i))
print(b)

def part1(b):
    x = int(0)
    y = int(0)
    while (x + y) != 2020:
        for i in b:
            x = i
            if (x + y) == 2020:
                print(x * y)
                break
            for i in b:
                y = i
                if (x + y) == 2020:
                    print(x * y)
                    break  

def part2(b):
    x = int(0)
    y = int(0)
    z = int(0)
    while (x + y + z) != 2020:
        for i in b:
            x = i
            if (x + y + z) == 2020:
                print(x * y * z)
                break
            for i in b:
                y = i
                if (x + y + z) == 2020:
                    print(x * y * z)
                    break
                for i in b:
                    z = i
                    if (x + y + z) == 2020:
                        print(x * y * z)
                        break

part2(b)