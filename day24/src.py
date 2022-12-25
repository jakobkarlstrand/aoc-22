import math
from decimal import *
from collections import deque, Counter
import re
from copy import deepcopy
from collections import defaultdict

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()

def parse_input():
    lines = read_input("day24/input.txt").splitlines()
    walls = set()
    blizzards = defaultdict()
    ground = set()

    for i,line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                walls.add((i,j))
            elif char in ["^", "v", "<", ">"]:
                if char == "^": delta = ((-1,0))
                elif char == "v": delta = ((1,0))
                elif char == ">": delta = ((0,1))
                elif char == "<": delta = ((0,-1))
                blizzards[(i,j)] = {
                    "current_pos": (i,j),
                    "delta": delta
                }
                ground.add((i,j))
            elif char == ".":
                ground.add((i,j))
    return ground,walls,blizzards



GROUND,WALLS,blizzards = parse_input()

def neighbors(pos):
    return [(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)]

def printGround(ground, maxWallX, maxWallY,current_pos, blizzards):
    for row in range(maxWallY+1):
        row_str = ""
        for col in range(maxWallX+1):
            
            if (row,col) in blizzards:
                row_str += "B"
            elif (row,col) == current_pos:
                row_str += "E"
            elif (row,col) in WALLS:
                row_str += "#"
            
            elif (row,col) in ground:
                row_str += "."
            
        print(row_str)
    print("\n\n")

def coors_connecting(start,end,ground,visited,dist):
    if start == end:
        return dist
    
    ns = [n for n in neighbors(start) if n not in visited and n in ground]
    if len(ns) == 0:
        return -1

    for n in ns:
        visited_copy = visited.copy()
        visited_copy.add(n)
        d = coors_connecting(n,end,ground,visited_copy,dist+1)
        if d > -1:
            return d
    return -1


def p1():
    minute = 0
    

    B_X = []
    B_Y = []

    min_wall_col = min([c[1] for c in WALLS ])
    max_wall_col = max([c[1] for c in WALLS ])
    min_wall_row = min([c[0] for c in WALLS ])
    max_wall_row = max([c[0] for c in WALLS ])

    GROUND_SIZE_X = max_wall_col-min_wall_col -1
    GROUND_SIZE_Y = max_wall_row - min_wall_row-1

    print(GROUND_SIZE_X,GROUND_SIZE_Y)




    for n in range(GROUND_SIZE_X):
        x_bliz = set()
        for bliz in blizzards:
            delta = blizzards[bliz]['delta']
            if delta[0] != 0:
                continue
            new_col = ((bliz[1]-1)+n*delta[1]) % GROUND_SIZE_X +1
            if new_col == 0:
                new_col = 1
            x_bliz.add((bliz[0],new_col))
        B_X.append(x_bliz)

    for n in range(GROUND_SIZE_Y):
        y_bliz = set()
        for bliz in blizzards:
            delta = blizzards[bliz]['delta']
            if delta[1] != 0:
                continue
            new_pos = ((bliz[0]-1)+n*delta[0]) % GROUND_SIZE_Y+1
            if new_pos == 0:
                new_pos = 1
            y_bliz.add((new_pos,bliz[1]))
        B_Y.append(y_bliz)

    dest = (max_wall_row,max_wall_col-1)
    start = (min_wall_row,min_wall_col+1)
    MOVE_STATE = (start,0, 0, []) # Pos, minute, times,stayed, path
    Q = deque()
    Q.append(MOVE_STATE)
    best_minute = 9999
    best_path = []
    visited = set()
    last_len = 0
    paths_found = 0
    GROUND_PER_ROUND = []
    least_square = GROUND_SIZE_Y*GROUND_SIZE_X
    for m in range(least_square):
        b = set([*B_X[(m) % GROUND_SIZE_X], *B_Y[(m) % GROUND_SIZE_Y]])
        GROUND_PER_ROUND.append(GROUND.difference(b))
    minute = 0
    all_open_grounds = set()
    dist = 0
    counter = Counter()
    while len(Q):
        pos, minute,times_stayed, path = Q.popleft()
        visited.add((pos,minute % GROUND_SIZE_X, minute % GROUND_SIZE_Y))
        counter.update([str(pos)])

        if minute > best_minute:
            continue

        if pos == dest:
            if minute <= best_minute:
                best_minute = minute
                best_path = path
            paths_found+=1
            #print(minute)
            continue
        

        ground_next_round = GROUND_PER_ROUND[(minute+1) % len(GROUND_PER_ROUND)]
    

        next_moves = []
        for n in neighbors(pos):
            if n in ground_next_round:
                next_moves.append(n)
        if len(next_moves) == 0:
            if pos in ground_next_round:
                next_moves.append(pos)

        print(pos)

        
        for n in next_moves:
            if (pos,(minute+1) % GROUND_SIZE_X, (minute+1) % GROUND_SIZE_Y) not in visited:
                Q.append((n,minute+1,0,[*path, pos]))

            

    
    # for mi,p in enumerate(best_path):
    #     ground_current_round = GROUND.difference(set([*B_X[(mi) % GROUND_SIZE_X], *B_Y[(mi) % GROUND_SIZE_Y]]))
    #     print(mi)
    #     printGround(ground_current_round,max_wall_col,max_wall_row,p, set([*B_X[mi%GROUND_SIZE_X],*B_Y[mi%GROUND_SIZE_Y]]))
    #     print("\n\n")
    print(best_minute)
    print("Paths found", paths_found)


def test():
    minute = 0
    

    B_X = []
    B_Y = []

    min_wall_col = min([c[1] for c in WALLS ])
    max_wall_col = max([c[1] for c in WALLS ])
    min_wall_row = min([c[0] for c in WALLS ])
    max_wall_row = max([c[0] for c in WALLS ])

    GROUND_SIZE_X = max_wall_col-min_wall_col -1
    GROUND_SIZE_Y = max_wall_row - min_wall_row-1

    print(GROUND_SIZE_X,GROUND_SIZE_Y)




    for n in range(GROUND_SIZE_X):
        x_bliz = set()
        for bliz in blizzards:
            delta = blizzards[bliz]['delta']
            if delta[0] != 0:
                continue
            new_col = ((bliz[1]-1)+n*delta[1]) % GROUND_SIZE_X +1
            if new_col == 0:
                new_col = 1
            x_bliz.add((bliz[0],new_col))
        B_X.append(x_bliz)

    for n in range(GROUND_SIZE_Y):
        y_bliz = set()
        for bliz in blizzards:
            delta = blizzards[bliz]['delta']
            if delta[1] != 0:
                continue
            new_pos = ((bliz[0]-1)+n*delta[0]) % GROUND_SIZE_Y+1
            if new_pos == 0:
                new_pos = 1
            y_bliz.add((new_pos,bliz[1]))
        B_Y.append(y_bliz)

    dest = (max_wall_row,max_wall_col-1)
    start = (min_wall_row,min_wall_col+1)
    MOVE_STATE = (start,0, 0, []) # Pos, minute, times,stayed, path
    Q = deque()
    Q.append(MOVE_STATE)
    best_minute = 9999
    best_path = []
    visited = set()


    GROUND_PER_ROUND = []
    least_square = GROUND_SIZE_Y*GROUND_SIZE_X
    for m in range(least_square):
        b = set([*B_X[(m) % GROUND_SIZE_X], *B_Y[(m) % GROUND_SIZE_Y]])
        GROUND_PER_ROUND.append(GROUND.difference(b))
    minute = 0
    paths = defaultdict()
    dest_reached = False
    while not dest_reached:
        ground_next_round = GROUND_PER_ROUND[(minute) % len(GROUND_PER_ROUND)]
    

        restart = False
        for pos in ground_next_round:
            if len(paths) == 0 or restart:
                paths[pos] = [pos]
                restart = True
                continue
            keys_to_pop = []
            paths_to_add = []
            for key in paths:
                    
                    dst = abs(pos[0]-key[0])+abs(pos[1]-key[1])
                    
                    if dst <= 1:
                        if pos == dest and start in paths[key]:
                            dest_reached = True
                        paths_to_add.append([*paths[key],pos])
                    keys_to_pop.append(key)
            for k in keys_to_pop:
                paths.pop(k)
            for p in paths_to_add:
                if start not in p:
                    continue
                paths[p[-1]] = p
        
        
        minute += 1
    for key in paths:
        path = paths[key]
        if start in path and dest in path:
            print("HERE",path, len(path))
        

test()