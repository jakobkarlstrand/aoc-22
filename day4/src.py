def read_input(filepath):
    file = open(filepath, 'r')
    return file.readlines()
    

def part1():
    lines = read_input("day4/input.txt")
    found = 0
    for line in lines:
        [r1,r2] = line.split(",")
        [a,b] = r1.split("-")
        [x,y] = r2.split("-")

        a = int(a)
        b = int(b)
        x = int(x)
        y = int(y)

        if (a >= x and b <= y) or (x >= a and y <= b):
            found += 1


    print(found)

def part2():
    lines = read_input("day4/input.txt")
    found = 0
    for line in lines:
        [r1,r2] = line.split(",")
        [a,b] = r1.split("-")
        [x,y] = r2.split("-")

        a = int(a)
        b = int(b)
        x = int(x)
        y = int(y)

        if(a in range(x,y+1) or b in range(x,y+1) or x in range(a,b+1) or y in range(a,b+1)):
            found += 1


    print(found)

part2()