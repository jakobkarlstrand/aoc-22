def read_input(filepath):
    file = open(filepath, 'r')
    return file.readlines()


lines = read_input("day4/input.txt")
crates = {
    "1": ["D","M","S","Z","R","F","W","N"],
    "2": ["W","P","Q", "G", "S"],
    "3": ["W", "R","V", "Q", "F", "N", "J", "C"],
    "4": ["F", "Z", "P", "C", "G", "D", "L"],
    "5": ["T", "P", "S"],
    "6": ["H", "D", "F","W", "R", "L"],
    "7": ["Z", "N", "D", "C"],
    "8": ["W", "N", "R", "F", "V", "S", "J", "Q"],
    "9": ["R", "M", "S", "G", "Z", "W", "V"],
}

def part1():
    # MADE THe INPUT FORMAT FROM 'move X from a to b' INTO --> X-a:b
    for line in lines:
        splitted = line.split("-")
        n = splitted[0]

        [_from, _to] = splitted[1].split(":")
        _to = _to.replace("\n", "")
        for i in range(int(n)):
            crates[_to].append(crates[_from].pop())
        



    answer = ""
    for s in crates:
        answer += (crates[s][-1])
    print("PART1: ",answer)


def part2():
    # MADE THe INPUT FORMAT FROM 'move X from a to b' INTO --> X-a:b
    for line in lines:
        splitted = line.split("-")
        n = splitted[0]

        [_from, _to] = splitted[1].split(":")

        temp_arr = []
        for i in range(int(n)):
            temp_arr.append(crates[_from].pop())
        
        crates[_to.replace("\n", "")] += reversed(temp_arr)


    answer = ""
    for s in crates:
        answer += (crates[s][-1])
    print("PART2: ",answer)


part1()
