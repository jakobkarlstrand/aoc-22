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

screen_width = 40
current_pixel = 0
screen = ""

for instruction in instructions:
    noop = instruction[0] == "n"
    X = 0
    cycle_time = noop_time

    if not noop:
        _,X = instruction.split(" ")
        cycle_time = addx_time


    for c in range(cycle+1, cycle+cycle_time+1):
        if (c - 20) % 40 == 0:

            answer += c*register
        if current_pixel > 39:
            current_pixel = 0 
        if current_pixel in range(register-1,register+2):
            screen += "#"
        else:
            screen += "."
        current_pixel += 1

        

    
    register += int(X)
    cycle += cycle_time

out_str = ""
for i in range(len(screen)):
    if i % 40 == 0:
        out_str += "\n"
    out_str += screen[i]
print(out_str)
