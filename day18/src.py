import math
from decimal import *
import collections

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


def coor_is_not_trapped(coordinates,visited,current,MAX_VALS):
    min_x,max_x,min_y,max_y,min_z,max_z = MAX_VALS
    x,y,z = current
    neigbors = [c for c in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)] if c not in coordinates and c not in visited]
    visited.add(current)
    if x < min_x or x > max_x or y < min_y or y > max_y or z < min_z or z > max_z:
        return True

    if len(neigbors) == 0:
        return False
    n_not_trapped = 0
    
    for coor in neigbors:
        if coor_is_not_trapped(coordinates,visited,coor,MAX_VALS):
            return True
        
    return False
    

    


def p2():
    lines = read_input("input.txt").splitlines()
    coordinates = []


    for line in lines:

        x,y,z = line.strip().split(",")
        coordinates.append((int(x),int(y),int(z)))

    sides = len(coordinates)*6
    touching = 0

    for i in range(len(coordinates)-1):
        x1,y1,z1 = coordinates[i]
        for j in range(i,len(coordinates)):
            x2,y2,z2 = coordinates[j]

            dst = sorted([ abs(x1-x2),abs(y2-y1),abs(z2-z1)])
            
            if dst [0] == 0 and dst [1] == 0 and dst[2] == 1: #TOUCHING
                #print(dst)
                touching += 2
    
    min_z = float("inf")
    max_z = -float("inf")
    min_y = float("inf")
    max_y = -float("inf")
    min_x = float("inf")
    max_x = -float("inf")

    

    for x,y,z in coordinates:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if z < min_z:
            min_z = z
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z

    print(min_x,max_x,min_y,max_y,min_z,max_z)
    
    set_coor = set(coordinates)
    
    

    trapped_set = set()

    for x in range(min_x,max_x+1):
        for y in range(min_y, max_y+1):
            for z in range(min_z,max_z+1):
                visited = set()
                if (x,y,z) not in coordinates:
                    if not coor_is_not_trapped(coordinates,visited,(x,y,z),[min_x,max_x,min_y,max_y,min_z,max_z]):
                        trapped_set.add((x,y,z))
    
    print(trapped_set)

            
    trapped_coordinates = list(trapped_set)
    touching_trapped = 0

    for i in range(len(trapped_coordinates)):
        x1,y1,z1 = trapped_coordinates[i]
        for j in range(0,len(coordinates)):
            x2,y2,z2 = coordinates[j]

            dst = sorted([ abs(x1-x2),abs(y2-y1),abs(z2-z1)])
            
            if dst [0] == 0 and dst [1] == 0 and dst[2] == 1: #TOUCHING
                #print(dst)
                touching_trapped += 1

            # Not connecting if at least one side is 0
    print(trapped_set)
    print(sides-touching-touching_trapped)

def p1():
    lines = read_input("input.txt").splitlines()
    coordinates = []



    for line in lines:
        print(line.strip().split(","))
        x,y,z = line.strip().split(",")
        coordinates.append((int(x),int(y),int(z)))

    sides = len(coordinates)*6
    touching = 0

    for i in range(len(coordinates)-1):
        x1,y1,z1 = coordinates[i]
        for j in range(i,len(coordinates)):
            x2,y2,z2 = coordinates[j]

            dst = sorted([ abs(x1-x2),abs(y2-y1),abs(z2-z1)])
            
            if dst [0] == 0 and dst [1] == 0 and dst[2] == 1: #TOUCHING
                #print(dst)
                touching += 2
        
        
                

            # Not connecting if at least one side is 0
    print(sides-touching)
p1()
p2()


