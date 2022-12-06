def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


def part1():
    sequence = read_input("day6/input.txt")
    length_message = 3
    idx = 3

    while idx < len(sequence):
        arr = list(sequence[idx-length_message:idx+1])
   

        s = set(arr)

        if len(s) == len(arr): #Unique
            print("ANSWER:",idx+1)
            break
        else:
            idx+=1


    
def part2():
    sequence = read_input("day6/input.txt")
    length_message = 13
    idx = 13

    while idx < len(sequence):
        arr = list(sequence[idx-length_message:idx+1])
    

        s = set(arr)

        if len(s) == len(arr): #Unique
            print("ANSWER:",idx+1)
            break
        else:
            idx+=1

part1()
part2()