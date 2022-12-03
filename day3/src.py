def read_input(filepath):
    file = open(filepath, 'r')
    return file.readlines()
    
_a_ascii = 97
_A_ascii = 65

def part1():
        
    items_found = []
    for line in read_input("day3/input.txt"):
        mid = len(line) // 2
        first = line[0:mid]
        second = line[mid:-1]

        for char in first:
            if char in second:
                items_found.append(char)
                break
    points = 0
    for item in items_found:

        if ord(item) < _a_ascii: #CAPS
            points += (ord(item)-_A_ascii+27)

        else:
            points += (ord(item)-_a_ascii+1)


    print("ANSWER: " + str(points))

def part2():
    items_found = []
    lines= read_input("day3/input.txt")
    idx = 2

    while(idx < len(lines)):
        [first, second, third] = lines[idx-2:idx+1]
        
        for item in first:
            if item in second and item in third:
                items_found.append(item)
                break
        idx += 3
    points = 0
    for item in items_found:

        if ord(item) < 97: #CAPS
            points += (ord(item)-64+26)

        else:
            points += (ord(item)-96)


    print("ANSWER: " + str(points))
part1()
part2()