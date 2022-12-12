import math
from decimal import *
import collections


def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


elevations = "abcdefghijklmnopqrstuvwxyz"


def grid_from_input():
    lines = read_input("day12/input.txt").split("\n")
    grid = [[*line] for line in lines]
    return grid


def neighbors(grid, pos, visited):
    ns = []
    dirs = [(-1,0), (1,0), (0,1), (0,-1)]
    

    for coor in dirs:
        r1,c1 = pos[0]+coor[0],pos[1]+coor[1]

        if r1 >= 0 and r1 < len(grid) and c1 >= 0 and c1 < len(grid[0]) and (r1,c1) not in visited:
            
            ns.append((r1,c1))

    return ns


def p1():
    grid = grid_from_input()
    start = (-1,-1)
    end = (-1,-1)
    

    for r in range(0,len(grid)):
        for c in range(len(grid[0])):

            if grid[r][c] == "S":
                start = (r,c)
            if grid[r][c] == "E":
                end = (r,c)
    



    path = bfs(grid,start,end)

    print("ANSWER P1: ",len(path)-1)


def p2():
    grid = grid_from_input()
    start = (-1,-1)
    end = (-1,-1)
    

    for r in range(0,len(grid)):
        for c in range(len(grid[0])):

            if grid[r][c] == "S":
                start = (r,c)
            if grid[r][c] == "E":
                end = (r,c)
    
    all_paths_lengts = []
    
    a_elevation_positions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in ["S", "a"]:
                a_elevation_positions.append((r,c))
            if grid[r][c] == "S":
                grid[r][c] = "a"

    for pos in a_elevation_positions:
        grid[pos[0]][pos[1]] = "S"
        path = bfs(grid,pos,end)
        if path:

            path_length = len(bfs(grid,pos,end))-1
            all_paths_lengts.append(path_length)
        grid[pos[0]][pos[1]] = "a"

    print("ANSWER P2: ",min(all_paths_lengts))

   


            

def bfs(grid, start, goal):
    
    queue = collections.deque([[start]])
    

    seen = set()
    seen.add(start)
    
    while queue:
        
        path = queue.popleft()
        r, c = path[-1]
        if r == goal[0] and c == goal[1]:
            return path
        current_height = elevations.index("a") if grid[r][c] == "S" else elevations.index(grid[r][c])
        
        for r2, c2 in neighbors(grid,(r,c),seen):

            next_height = elevations.index("z") if grid[r2][c2] == "E" else elevations.index(grid[r2][c2])
            if next_height - current_height <= 1:
                queue.append(path + [(r2, c2)])
                seen.add((r2, c2))

        
# v..v<<<<
# >v.vv<<^
# .v.v>E^^
# .>v>>>^^
# ..>>>>>^
    
# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

p1()
p2()