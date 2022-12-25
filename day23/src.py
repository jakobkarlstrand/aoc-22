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
    lines = read_input("day23/input.txt").splitlines()
    elves = set()
    for row,line in enumerate(lines):
        for col,char in enumerate(line):
        
            if char == "#":
                elves.add((row,col))

    return elves

def east_neighbors(row,col):

    return [(row-1,col+1),(row,col+1),(row+1,col+1)]     

def west_neighbors(row,col):

    return [(row-1,col-1),(row,col-1),(row+1,col-1)]

def south_neighbors(row,col):

    return [(row+1,col-1),(row+1,col),(row+1,col+1)]

def north_neighbors(row,col):

    return [(row-1,col-1),(row-1,col),(row-1,col+1)]

def neighbors(row,col):
    
    return north_neighbors(row,col) + east_neighbors(row,col) + south_neighbors(row,col) + west_neighbors(row,col)

def print_coordinates(coordinates):
    min_row = min([pos[0] for pos in coordinates])
    max_row = max([pos[0] for pos in coordinates])
    min_col = min([pos[1] for pos in coordinates])
    max_col = max([pos[1] for pos in coordinates])
    for row in range(min_row-5,max_row+5):
        row_str = ""
        for col in range(min_col-5,max_col+5):
            if (row,col) in coordinates:
                row_str += "#"
            else:
                row_str += "."
        print(row_str)


def p1():

    elves_positions = parse_input()

    order_idx = [0,1,2,3]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    

                

    

    for i in range(10):
        new_positions = defaultdict()

        for row,col in elves_positions:
            elf_nearby = False
            for n_row,n_col in neighbors(row,col):
                if (n_row,n_col) in elves_positions:
                    elf_nearby = True
                    break
            # North 0, South = 1, West = 2, East = 3
            order = [north_neighbors(row,col), south_neighbors(row,col), west_neighbors(row,col), east_neighbors(row,col)]
            if elf_nearby: #Move 
                
                found = False
                for idx in order_idx:
                    
                    if len([v for v in order[idx] if v in elves_positions]) == 0:
                        delta = directions[idx]
                        new_positions[(row,col)] = (row+delta[0],col+delta[1])
                        found = True
        
                        break
                if not found:
                    new_positions[(row,col)] = (row,col)

            else:
                new_positions[(row,col)] = (row,col) #Stay

            
            #check new positions
        all_new_position = [new_positions[v] for v in new_positions]
        
        
        for key in new_positions:
            count = len([pos for pos in all_new_position if pos == new_positions[key]])
    
            if not count > 1:
                elves_positions.remove(key)
                elves_positions.add(new_positions[key])
                
                


        #Change order
        order_pop = order_idx.pop(0)
        order_idx = [*order_idx,order_pop]

    
                
    
    min_row = min([pos[0] for pos in elves_positions])
    max_row = max([pos[0] for pos in elves_positions])
    min_col = min([pos[1] for pos in elves_positions])
    max_col = max([pos[1] for pos in elves_positions])
    total_tiles = abs(max_row-min_row+1)*abs(max_col-min_col+1)
    print("ANSWER P1: ", total_tiles - len(elves_positions))
    
        



def p2():
    elves_positions = parse_input()
    
    order_idx = [0,1,2,3]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]


                

    round_count = 0

    while True:
        new_positions = defaultdict()
        no_elf_moved = True
        for row,col in elves_positions:
            elf_nearby = False
            for n_row,n_col in neighbors(row,col):
                if (n_row,n_col) in elves_positions:
                    elf_nearby = True
                    break
            # North 0, South = 1, West = 2, East = 3
            order = [north_neighbors(row,col), south_neighbors(row,col), west_neighbors(row,col), east_neighbors(row,col)]
            if elf_nearby: #Move 
                
                found = False
                for idx in order_idx:
                    
                    if len([v for v in order[idx] if v in elves_positions]) == 0:
                        delta = directions[idx]
                        new_positions[(row,col)] = (row+delta[0],col+delta[1])
                        found = True
                        no_elf_moved = False
                        break
                if not found:
                    new_positions[(row,col)] = (row,col)

            else:
                new_positions[(row,col)] = (row,col) #Stay

            
            #check new positions
        valid_positions = set()
        not_valid = set()
        for key in new_positions:
            if new_positions[key] in not_valid:
                continue
            elif new_positions[key] in valid_positions:
                valid_positions.remove(new_positions[key])
                not_valid.add(new_positions[key])
            else:
                valid_positions.add(new_positions[key])
    
        
        
        for key in new_positions:
            
    
            if key != new_positions[key] and new_positions[key] in valid_positions:
                elves_positions.remove(key)
                elves_positions.add(new_positions[key])

        #Change order
        order_pop = order_idx.pop(0)
        order_idx = [*order_idx,order_pop]
        round_count += 1
        print(round_count)
        if no_elf_moved:
            break

    
                
    
    min_row = min([pos[0] for pos in elves_positions])
    max_row = max([pos[0] for pos in elves_positions])
    min_col = min([pos[1] for pos in elves_positions])
    max_col = max([pos[1] for pos in elves_positions])
    total_tiles = abs(max_row-min_row+1)*abs(max_col-min_col+1)
    print("ANSWER P1: ", total_tiles - len(elves_positions))




    
p2()