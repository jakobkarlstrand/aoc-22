import math
from decimal import *
import collections

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()

def get_rock_coordinates(shape,tallest_rock):
    tallest_y = tallest_rock[1]
    offset = 4
    if shape == "hori":

        return [(-1,tallest_y+offset),(0,tallest_y+offset),(1,tallest_y+offset),(2,tallest_y+offset)] # SHAPE:   -
    
    if shape == "plus":

        return [(-1,tallest_y+offset+1),(0,tallest_y+offset),(0,tallest_y+offset+1),(0,tallest_y+offset+2),(1,tallest_y+offset+1)] # SHAPE:   +
    if shape == "el":

        return [(-1,tallest_y+offset),(0,tallest_y+offset),(1,tallest_y+offset),(1,tallest_y+offset+1),(1,tallest_y+offset+2)] # SHAPE:   L
         


    if shape == "vert":

        return [(-1,tallest_y+offset),(-1,tallest_y+offset+1),(-1,tallest_y+offset+2),(-1,tallest_y+offset+3)] # SHAPE:   l
    if shape == "hash":

        return [(-1,tallest_y+offset),(-1,tallest_y+offset+1),(0,tallest_y+offset),(0,tallest_y+offset+1)] # SHAPE:   #

    
def move(dir, coors):
    delta = (0,0)
    if dir == "left":
        delta = (-1,0)
    elif dir == "right":
        delta = (1,0)
    elif dir == "down":
        delta = (0,-1)
    new_coors = []
    for coor in coors:
        new_coors.append((coor[0]+delta[0], coor[1]+delta[1]))
    return new_coors

def p1():
    JET_GAS = read_input("day17/input.txt")
    GAS_TRANSLATE = {
        ">" : "right",
        "<" : "left"
    }

    GAS_LENGTH = len(JET_GAS)
    move_idx = 0

    shapes = ["hori","plus","el","vert", "hash"]
    SHAPES_LENGTH = len(shapes)
    shape_idx = 0
    
    TUNNEL_START_END = (-3,3)
            


    

    rock_coordinates = set()
    tallest_rock = (0,0)
    lowest_rock = (0,0)
    n_rocks = 1
    
    current_rock_coordinates = get_rock_coordinates(shapes[0],tallest_rock)
    while n_rocks < 1_000_000_000:
        if n_rocks % 1_000_000 == 0:
            print(n_rocks/1_000_000_000*100)
    
        place_rock = False
        coors_after_jetgas = move(GAS_TRANSLATE[JET_GAS[move_idx]],current_rock_coordinates)
        update_move_index = True
        for coor in coors_after_jetgas:
            if coor[0] > TUNNEL_START_END[1] or coor[0] < TUNNEL_START_END[0] or coor in rock_coordinates:
                coors_after_jetgas = [*current_rock_coordinates]
                update_move_index = False
        
        coors_after_move_down = move("down", coors_after_jetgas)


        for coor in coors_after_move_down:
            if coor in rock_coordinates or coor[1] <= 0:
                coors_after_move_down = [*coors_after_jetgas]
                place_rock = True
                update_move_index = False

        move_idx += 1
        if move_idx >= GAS_LENGTH:
            move_idx = 0

        if place_rock:
            local_tallest = (0,-float("inf"))
            for coor in coors_after_move_down:
                rock_coordinates.add(coor)
                if coor[1] > local_tallest[1]:
                    local_tallest = coor
            if local_tallest[1] > tallest_rock[1]:
                tallest_rock = local_tallest
            n_rocks += 1
            if abs(lowest_rock[1]-tallest_rock[1]) >= 10:
                rock_coordinates = set([rock for rock in rock_coordinates if abs(rock[1]-tallest_rock[1]) <= 10])
            shape_idx += 1
            
    
            if shape_idx >= SHAPES_LENGTH:
                shape_idx = 0
            current_rock_coordinates = get_rock_coordinates(shapes[shape_idx],tallest_rock)
        else:
            current_rock_coordinates = [*coors_after_move_down]
        
    
    print(tallest_rock)

def find_pattern():

    JET_GAS = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    GAS_TRANSLATE = {
        ">" : "right",
        "<" : "left"
    }

    GAS_LENGTH = len(JET_GAS)
    move_idx = 0

    shapes = ["hori","plus","el","vert", "hash"]
    SHAPES_LENGTH = len(shapes)
    shape_idx = 0
    
    TUNNEL_START_END = (-3,3)

def p2():
    JET_GAS = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    GAS_TRANSLATE = {
        ">" : "right",
        "<" : "left"
    }

    GAS_LENGTH = len(JET_GAS)
    move_idx = 0

    shapes = ["hori","plus","el","vert", "hash"]
    SHAPES_LENGTH = len(shapes)
    shape_idx = 0
    
    TUNNEL_START_END = (-3,3)
            


    

    rock_coordinates = set()
    tallest_rock = (0,0)
    n_rocks = 1
    first_n_rocks = 0
    height_diff = 0
    current_rock_coordinates = get_rock_coordinates(shapes[0],tallest_rock)

    first_height = 0
    diff_rocks = 0
    while n_rocks < 1000000:

        if move_idx == 0 and n_rocks != 1:

            if first_height == 0:
                first_height = tallest_rock[1]
                first_n_rocks = n_rocks
            else:
                height_diff = tallest_rock[1]-first_height
                diff_rocks = n_rocks - first_n_rocks
                for y in range(-5,10):
                    row_str = ""
                    for x in range(-3,4):
                        row_str += "#" if (x,tallest_rock[1]- y) in rock_coordinates else "."
                    print(row_str)
                print("\n\n")
                # print("F HEIGHT ", first_height)
                # print("H DIFF ", height_diff)
                # print("FIRST ROCKS: ",first_n_rocks)
                # print("DIFF ROCKS " ,diff_rocks)
                # print("SIGN: ", shapes[shape_idx])
                
        place_rock = False
        coors_after_jetgas = move(GAS_TRANSLATE[JET_GAS[move_idx]],current_rock_coordinates)
        update_move_index = True
        for coor in coors_after_jetgas:
            if coor[0] > TUNNEL_START_END[1] or coor[0] < TUNNEL_START_END[0] or coor in rock_coordinates:
                coors_after_jetgas = [*current_rock_coordinates]
                update_move_index = False
        
        coors_after_move_down = move("down", coors_after_jetgas)


        for coor in coors_after_move_down:
            if coor in rock_coordinates or coor[1] <= 0:
                coors_after_move_down = [*coors_after_jetgas]
                place_rock = True
                update_move_index = False

        move_idx += 1
        if move_idx >= GAS_LENGTH:
            move_idx = 0

        if place_rock:
            local_tallest = (0,0)
            for coor in coors_after_move_down:
                rock_coordinates.add(coor)
                if coor[1] > local_tallest[1]:
                    local_tallest = coor
            if local_tallest[1] > tallest_rock[1]:
                tallest_rock = local_tallest
            n_rocks += 1
            shape_idx += 1
                
        

    
            if shape_idx >= SHAPES_LENGTH:
                shape_idx = 0
            current_rock_coordinates = get_rock_coordinates(shapes[shape_idx],tallest_rock)
        else:
            current_rock_coordinates = [*coors_after_move_down]
        
    
    # LIMIT_ROCKS = 1000000000000-first_n_rocks
    # h = first_height
    # # per diff_rocks there is a height of height_diff
    # print("MOD",LIMIT_ROCKS % diff_rocks)
    # h += (LIMIT_ROCKS // diff_rocks)*(height_diff+1)
    # print(h)
    # print(1514285714288)
    # n_rocks = first_n_rocks
    # height = first_height



p1()