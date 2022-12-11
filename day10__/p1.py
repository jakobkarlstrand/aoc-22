import math

def read_input(filepath):
    file = open(filepath, 'r')
    return [f.strip() for f in file.readlines()]

instructions = read_input("day10/input.txt")

noop_time = 1
addx_time = 2

answer = 0
cycle = 0
register = 1

for instruction in instructions:
    noop = instruction[0] == "n"
    X = 0
    cycle_time = noop_time

    if not noop:
        _,X = instruction.split(" ")
        cycle_time = addx_time


    for c in range(cycle+1, cycle+cycle_time+1):
        if (c - 20) % 40 == 0:
            print(c,register)
            answer += c*register
    
    register += int(X)
    cycle += cycle_time
    
print(answer)