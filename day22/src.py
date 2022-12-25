import math
from decimal import *
import collections
import re
from copy import deepcopy
from collections import defaultdict

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()

def parse_input():
    lines = read_input("day22/input.txt")
    raw_map,instructions = lines.split("\n\n")

    map = defaultdict()

    width_for_row = defaultdict()
    height_for_col = defaultdict()
    
    for row,line in enumerate(raw_map.splitlines()):
        
        width_count = 0
        for col,char in enumerate(line):
            if char == ".":
                map[(row,col)] = 0
                width_count+=1
            elif char == "#":
                map[(row,col)] = 1
                width_count+=1
        width_for_row[row] = width_count


    max_length = max([len(s) for s in raw_map.splitlines()])
            
    heights_col = [[9999,-1] for _ in range(max_length)]

    for key in map:
        row = key[0]
        col = key[1]
        if row < heights_col[col][0]:
            heights_col[col][0] = row
        if row > heights_col[col][0]:
            heights_col[col][1] = row
    

    for i,(lo,hi) in enumerate(heights_col):
        height_for_col[i] = hi-lo+1


    inst = []
    s = ""
    for char in instructions:
        if char != "R" and char != "L":
            s+= char
        else:
            if s != "":
                inst.append(int(s))
                s = ""
            inst.append(char)
    if s != "":
        inst.append(s)

    return map, inst,width_for_row,height_for_col




def start_pos():
    
    start_col = 999999
    for key in MAP:
        if MAP[key] == WALL or key[0] != 0:
            continue
        if key[1] < start_col:
            start_col = key[1]
    return (0,start_col)
            


def change_direction(current_direction_idx,left_right):
    delta = -1 if left_right == "L" else 1

    new_direction = current_direction_idx+delta
    if new_direction < 0:
        new_direction = 3
    elif new_direction > 3:
        new_direction = 0
    return DIRECTIONS[new_direction]


WALL = 1
FREE = 0

MAP, INSTRUCTIONS,WIDTH_FOR_ROW,HEIGHT_FOR_COL = parse_input()
DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)] #RIGHT DOWN LEFT UP

TRANSLATE_DIRECTION = {
    (0,1): "RIGHT",
    (1,0): "DOWN",
    (0,-1): "LEFT",
    (-1,0): "UP"
}


def get_next_coor_in_direction(position,direction):
    return (position[0]+direction[0],position[1]+direction[1])

def p1():

    PATH = defaultdict()
    position = start_pos()
    direction = DIRECTIONS[0]

    for inst in INSTRUCTIONS:
        if inst == "L" or inst == "R":
            direction = change_direction(DIRECTIONS.index(direction),inst)
            continue
        current_pos = position
        for _ in range(int(inst)): # moves
            next_move = get_next_coor_in_direction(current_pos,direction)

            
            if next_move in MAP:
                if MAP[next_move] == WALL:
                    position = current_pos
                    PATH[current_pos] = direction
                    break
                else:
                    current_pos = next_move
                    PATH[current_pos] = direction
                    continue
            else:
                if DIRECTIONS.index(direction) in [0,2]: #LEFT OR RIGHT
                    width = WIDTH_FOR_ROW[next_move[0]]
        
                    if DIRECTIONS.index(direction) == 0: #RIGHT
                        next_move = (next_move[0],next_move[1]-width)
                    else: #RIGHT
                        next_move = (next_move[0],next_move[1]+width)
                else:

                    height = HEIGHT_FOR_COL[next_move[1]]
    
                    if DIRECTIONS.index(direction) == 1: #DOWN

                        next_move = (next_move[0]-height,next_move[1])
                    else: #UP
                        next_move = (next_move[0]+height,next_move[1])
            
                if MAP[next_move] == WALL:
                    position = current_pos
                    PATH[current_pos] = direction
                    break
                else:
                    current_pos = next_move
                    PATH[current_pos] = direction
                    continue
        position = current_pos

    answer = 1000*(position[0]+1) + 4*(position[1]+1) + DIRECTIONS.index(direction)

    print("ANSWER P1: ", answer)


def get_cube_sides(width,height, size):
    row = 0
    col = 0
    sides_found = 0
    sides = defaultdict()
    while sides_found < 7:
        all_in_map = True
        coordinates = []
        for r in range(row,row+size):
            for c in range(col,col+size):
                if (r,c) not in MAP:
                    all_in_map = False
                    break
                coordinates.append((r,c))
            if not all_in_map:
                break
        if all_in_map:
            sides[str(sides_found+1)] = coordinates
            sides_found += 1
        col += size

        if col > width:
            row += size
            col = 0
        if row > height:
            break

    return sides

SIDES_RELATIONSHIP = {
    "1":{
        "RIGHT": "2",
        "DOWN": "3",
        "LEFT": "4",
        "UP": "6"
    },
    "2":{
        "RIGHT": "5",
        "LEFT": "1",
        "DOWN": "3",
        "UP": "6"
    },
    "3":{
        "RIGHT": "2",
        "LEFT": "4",
        "DOWN": "5",
        "UP": "1"
    },
    "4":{
        "RIGHT": "5",
        "LEFT": "1",
        "DOWN": "6",
        "UP": "3"
    },
    "5":{
        "RIGHT": "2",
        "LEFT": "4",
        "DOWN": "6",
        "UP": "3"
    },
    "6":{
        "RIGHT": "5",
        "LEFT": "1",
        "DOWN": "2",
        "UP": "4"
    }
}

def p2():

    PATH = defaultdict()
    position = start_pos()
    direction = DIRECTIONS[0]


    max_width = max([key[1] for key in MAP])
    max_height= max([key[0] for key in MAP])

    FACE_SIZE = 50
    SIDES = get_cube_sides(max_width,max_height,FACE_SIZE)
    
    
    # row_idx = 0
    # for row in range(max_height+1):
    #     row_str = ""
    #     for col in range(max_width+1):
    #         found = False
    #         for key in SIDES:
    #             if (row,col) in SIDES[key]:
    #                 row_str += str(key)
    #                 found = True
    #                 break
    #         if not found:
    #             row_str += " "
        

    #     row_str = row_str.replace(" "*FACE_SIZE, " ")
    #     row_str = row_str.replace("1"*FACE_SIZE, "1")
    #     row_str = row_str.replace("2"*FACE_SIZE, "2")
    #     row_str = row_str.replace("3"*FACE_SIZE, "3")
    #     row_str = row_str.replace("4"*FACE_SIZE, "4")
    #     row_str = row_str.replace("5"*FACE_SIZE, "5")
    #     row_str = row_str.replace("6"*FACE_SIZE, "6")
    #     if row_idx % FACE_SIZE == 0:

    #         print(row_str)
    #     row_idx += 1

            

    for inst in INSTRUCTIONS:
        if inst == "L" or inst == "R":
            direction = change_direction(DIRECTIONS.index(direction),inst)
            continue
        current_pos = position
        for _ in range(int(inst)): # moves
            next_move = get_next_coor_in_direction(current_pos,direction)

            
            if next_move in MAP:
                if MAP[next_move] == WALL:
                    position = current_pos
                    PATH[current_pos] = direction
                    break
                else:
                    current_pos = next_move
                    PATH[current_pos] = direction
                    continue
            else:
                current_side = str([key for key in SIDES if current_pos in SIDES[key]][0])
                next_side = None

                direction_text = TRANSLATE_DIRECTION[direction]

                next_side = SIDES_RELATIONSHIP[current_side][direction_text]

                outgoing_direction = TRANSLATE_DIRECTION[direction]
                
                incoming_direction_opposite = [s for s in SIDES_RELATIONSHIP[next_side] if SIDES_RELATIONSHIP[next_side][s] == current_side][0]
                incoming_direction = ""
                if incoming_direction_opposite == "RIGHT":
                    incoming_direction = "LEFT"

                elif incoming_direction_opposite == "LEFT":
                    incoming_direction = "RIGHT"

                elif incoming_direction_opposite == "UP":
                    incoming_direction = "DOWN"

                elif incoming_direction_opposite == "DOWN":
                    incoming_direction = "UP"
        
                min_row_current_side = min([c[0] for c in SIDES[current_side]])
                min_col_current_side = min([c[1] for c in SIDES[current_side]])
                max_row_current_side = max([c[0] for c in SIDES[current_side]])
                max_col_current_side = max([c[1] for c in SIDES[current_side]])

                min_row_next_side = min([c[0] for c in SIDES[next_side]])
                min_col_next_side = min([c[1] for c in SIDES[next_side]])
                max_row_next_side = max([c[0] for c in SIDES[next_side]])
                max_col_next_side = max([c[1] for c in SIDES[next_side]])

                current_steps_row = min_row_current_side - current_pos[0]
                current_steps_col = min_col_current_side - current_pos[1]
                next_row = -1
                next_col = -1
                passed = False
                if incoming_direction == "LEFT":
                    next_col = max_col_next_side
                    
                    if outgoing_direction == incoming_direction:
                        next_row = min_row_next_side + current_steps_row
                    elif outgoing_direction == "UP":
                        next_row = max_row_next_side - current_steps_col
                    elif outgoing_direction == "DOWN":
                        next_row = min_row_next_side + current_steps_col
                    passed = True
                elif incoming_direction == "RIGHT":
                    
                    next_col = min_col_next_side

                    if outgoing_direction == incoming_direction:
                        next_row = min_row_next_side + current_steps_row
                    elif outgoing_direction == "UP":
                        next_row = min_row_next_side + current_steps_col
                    elif outgoing_direction == "DOWN":
                        next_row = max_row_next_side - current_steps_col
                    passed =True
                
                elif incoming_direction == "UP":
                    next_row = max_row_next_side

                    if outgoing_direction == incoming_direction:
                        next_col = min_col_next_side + current_steps_col
                    elif outgoing_direction == "RIGHT":
                        next_col = min_col_next_side + current_steps_row
                    elif outgoing_direction == "LEFT":
                        next_col = max_col_next_side - current_steps_row
                    passed = True
                elif incoming_direction == "DOWN":
                    next_row = min_row_next_side

                    if outgoing_direction == incoming_direction:
                        next_col = min_col_next_side + current_steps_col
                    elif outgoing_direction == "RIGHT":
                        next_col = min_col_next_side + current_steps_row
                    elif outgoing_direction == "LEFT":
                        next_col = max_col_next_side - current_steps_row
                    passed = True

                print(passed)

                

                


                        


                # if incoming_direction == outgoing_direction:
                #     if incoming_direction == "UP":
                #         next_row = max_row_next_side
                #         next_col =  min_col_next_side + current_steps_col
                #     elif incoming_direction == "DOWN":
                #         next_row = min_row_next_side
                #         next_col =  min_col_next_side + current_steps_col
                #     elif incoming_direction == "LEFT":
                #         next_row = min_row_next_side + current_steps_row
                #         next_col =  max_col_next_side
                #     elif incoming_direction == "RIGHT":
                #         next_row = min_row_next_side + current_steps_row
                #         next_col =  min_col_next_side


            
                # elif incoming_direction in ["RIGHT", "LEFT"] and outgoing_direction in ["RIGHT", "LEFT"]:
                #     next_row = max_row_next_side - current_steps_row
                #     next_col =  max_col_next_side
                        

                # elif incoming_direction == "UP" and outgoing_direction == "RIGHT":
                #     next_row = max_row_next_side
                #     next_col = min_col_next_side + current_steps_row
                # elif incoming_direction == "DOWN" and outgoing_direction == "LEFT":
                #     next_row = min_row_next_side
                #     next_col = min_col_next_side + current_steps_row

                # elif incoming_direction == "UP" and outgoing_direction == "RIGHT":
                #     next_col = max_col_next_side
                #     next_row = min_row_next_side + current_steps_col
                # elif outgoing_direction == "UP" and incoming_direction == "RIGHT":
                #     next_row = min_row_next_side + current_steps_col
                #     next_col = min_col_next_side

                # elif outgoing_direction == "LEFT" and incoming_direction == "DOWN":
                #     next_row = min_row_next_side
                #     next_col = min_col_next_side + current_steps_row 

                print("OPPOSITE",incoming_direction_opposite)
                print("OUTGOIING",outgoing_direction)
                print("INCOMING", incoming_direction)
                print("\n\n")
                
                next_move = (next_row,next_col)



            
                if MAP[next_move] == WALL:
                    position = current_pos
                    PATH[current_pos] = direction
                    break
                else:
                    current_pos = next_move
                    
                    direction = [coor for coor in TRANSLATE_DIRECTION if TRANSLATE_DIRECTION[coor] == incoming_direction][0]
                    PATH[current_pos] = direction
                    continue
        position = current_pos

    answer = 1000*(position[0]+1) + 4*(position[1]+1) + DIRECTIONS.index(direction)

    print("ANSWER P1: ", answer)





p2()

