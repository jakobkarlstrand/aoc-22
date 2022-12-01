def read_input(filepath):
    file = open(filepath, 'r')
    return file.readlines()
    


def part1():
    list_cal = []
    cals = 0
    for calories in read_input("day1/input.txt"):
        if calories == "\n":
            list_cal.append(cals)
            cals = 0
            continue
        cals += int(calories)
    list_cal.append(cals)

    print(max(list_cal))

def part2():
    list_cal = []
    cals = 0
    for calories in read_input("day1/input.txt"):
        if calories == "\n":
            list_cal.append(cals)
            cals = 0
            continue
        cals += int(calories)
    list_cal.append(cals)


    top3 = 0

    for i in range(3):
        max_val = max(list_cal)
        list_cal.pop(list_cal.index(max_val))
        top3+=max_val

    print(top3)


