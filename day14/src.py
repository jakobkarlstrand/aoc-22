import math
from decimal import *
import collections


def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


def parse_input():
    raw = read_input("day14/input.txt").splitlines()
    ranges_of_coordinates = []

    for line in raw:
        coordinates = line.split(" -> ")
        
        for idx in range(len(coordinates)-1):
            x1,y1 = coordinates[idx].split(",")
            x2,y2 = coordinates[idx+1].split(",")

            start_end = [(int(x1),int(y1)),(int(x2),int(y2))]
            ranges_of_coordinates.append(start_end)
    rocks = set()
    for start,end in ranges_of_coordinates:
        if start[0] > end[0] or start[1] > end[1]:
            [start,end] = [end,start]
        for x in range(start[0],end[0]+1):
            for y in range(start[1],end[1]+1):
                rocks.add((x,y))
    return rocks


def p1():

    occupied = parse_input()
    ORIGIN = (500,0)
    last_stone = max([c[1] for c in occupied]) + 2

    idx = 0
    answer = 0
    while answer == 0:
        sand = ORIGIN
        while True:

            if sand[1] >= last_stone:
                answer = idx
                break

            if (sand[0],sand[1]+1) not in occupied:
                sand = (sand[0],sand[1]+1)
            elif (sand[0]-1,sand[1]+1) not in occupied:
                sand = (sand[0]-1,sand[1]+1)
            elif (sand[0]+1,sand[1]+1) not in occupied:
                sand = (sand[0]+1,sand[1]+1)
            else:
                occupied.add(sand)
                break
        idx += 1
    print("PART1: ",answer)

def p2():
    occupied = parse_input()
    

    ORIGIN = (500,0)
    last_stone = max([c[1] for c in occupied]) + 2

    idx = 0
    answer = 0
    while answer == 0:
        sand = ORIGIN
        while True:

            down = (sand[0],sand[1]+1)
            left = (sand[0]-1,sand[1]+1)
            right = (sand[0]+1,sand[1]+1)

            if down not in occupied and down[1] < last_stone:
                sand = down
            elif left not in occupied and left[1] < last_stone:
                sand = left
            elif right not in occupied and right[1] < last_stone:
                sand = right
            else:
                occupied.add(sand)
                if idx > 0 and sand == ORIGIN:
                    answer = idx+1
                    
                break
        idx += 1
    print("PART2: ",answer)

p1()
p2()

