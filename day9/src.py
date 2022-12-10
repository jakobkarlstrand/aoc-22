import math

def read_input(filepath):
    file = open(filepath, 'r')
    return [f.strip() for f in file.readlines()]

def get_positions(n_knots):
    with open("day9/input.txt", "r") as ifile:
            instructions = read_input("day9/input.txt")

    moves = {"R":(1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}    
    positions = {f:[0,0] for f in range(n_knots)}

    visited =  set()

    for instruction in instructions:
        direction, steps = instruction.split(" ")
        vector = moves[direction]

        for _ in range(int(steps)):
            positions[0][0]+=vector[0]
            positions[0][1]+= vector[1]

            for idx in range(1,n_knots):
                x_diff = (positions[idx-1][0] - positions[idx][0])
                y_diff = (positions[idx-1][1] - positions[idx][1])

                if abs((positions[idx-1][0] - positions[idx][0])) + abs(positions[idx-1][1] - positions[idx][1]) < 3:
                    positions[idx][0] += int(x_diff/ 2)
                    positions[idx][1] += int(y_diff/ 2)
                else:
                    
                    min_dist = min(x_diff,y_diff, key=abs)
                    divider = abs(min_dist) if min_dist != 0 else 1

                    positions[idx][0] += round(((x_diff) / 2) + min_dist/divider)
                    positions[idx][1] += round(((y_diff) / 2) + min_dist/divider)

                    # x: 1 + 1*0.1 
# # # #
# # # H
# 2 1 #

# # # H
# # # 1
# 2 . #         
            visited.add(tuple(positions[len(positions)-1]))

    print("Answer: {}".format(len(visited)))

get_positions(n_knots=10)