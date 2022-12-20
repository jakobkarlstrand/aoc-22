import math
from decimal import *
import collections
from copy import deepcopy


def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


def parse_input():

    rates = {}
    exits = {}
    all_valves = []
    
    for line in read_input("input.txt").splitlines():
        [name_rate, valves] = line.split(";") 
        rate = int(name_rate.split("=")[1])
        name = name_rate.split(" has ")[0][-2:]
        valves = valves.split("valve")[1].split(",")
        paths = []
        for path in valves:
            if " " in path:
                paths.append(path.split(" ")[1])
            else:
                paths.append(path)
        rates[name] = rate
        exits[name] = paths
        all_valves.append(name)

        

    return [all_valves,rates,exits]

def bfs_find_distance(start,end,dst, visited):
    if start == end:
        return dst

    next_valves = [ex for ex in EXITS[start] if ex not in visited]
    visited.add(start)
    min_d = float("inf")
    for n in next_valves:
        d = bfs_find_distance(n, end, dst+1,visited)
        if d != -1 and d < min_d:
            min_d = d
    
    
    return min_d

def dist_between_valves(start,end):
    queue = [start]
    dst = 0
    visited = set()
    while len(queue):
        current = queue.pop(0)
        if current == end:
            break
        visited.add(current)
        next_valves = [ex for ex in EXITS[start] if ex not in visited]

        queue += next_valves
        



VALVES,RATES,EXITS = parse_input() #global
DISTANCES = {}
GOOD_VALVES = [v for v in VALVES if RATES[v] != 0]

for v1 in VALVES:
    inner_dict = {}
    for v2 in VALVES:
        dst = bfs_find_distance(v1,v2,0,set())
        print(dst)
        inner_dict[v2] = dst
    DISTANCES[v1] = inner_dict



def bfs_find_best_path(current,flow,minute,open_valves):
    if minute > 30:
        return flow
    
    next_valves = [ex for ex in EXITS[current] if ex not in open_valves and ex in GOOD_VALVES]

    best_score = 0
    for v in next_valves:
        score = bfs_find_best_path(v,flow,minute+1,open_valves)
        if best_score < score:
            best_score = score
    best_score_open = 0
    
    for v in next_valves:
        new_open = open_valves.copy()
        new_open.add(v)
        score = bfs_find_best_path(v,flow+((30-(minute+2))*RATES[v]),minute+1,new_open)
        if best_score_open < score:
            best_score_open = score
    return max(best_score_open,best_score)

    #DD --> BB --> JJ --> HH --> EE --> CC
def dfs_most_score(start,minute,flow,open, path):
    if minute <= 1:
        return [flow,path]
    
    flows = []
    ps = [] #Paths
    for v in GOOD_VALVES: #Valves to open
        if v in open:
            continue
        new_open = deepcopy(open)
        new_open.add(v)
        minute_lapsed = minute-(DISTANCES[start][v]+1)
        new_flow = flow + minute_lapsed*RATES[v]
        score,p = dfs_most_score(v,minute_lapsed,new_flow,new_open,[*path,v])
        flows.append(score)
        ps.append(p)
    if len(ps) == 0:
        return [flow,path]

    max_score = max(flows)
    wanted_p = ps[flows.index(max_score)]
    return [max_score,wanted_p]




def p1():
    minute = 30
    start = VALVES[0]
    open = set()
    flow = 0
    path = []

    print(dfs_most_score(start,30,0,open,[]))
    return

    while minute > 0:
        max_points = 0
        dest = start
        distance = 0
        path.append(start)
        for v in GOOD_VALVES:
            if v in open:
                continue
            dst = DISTANCES[start][v]
            curr_points = (minute-(dst+1))*RATES[v]
            if curr_points > max_points:
                max_points = curr_points
                dest = v
                distance = dst
        print(max_points)
        flow += max_points
        start = dest
        open.add(dest)
        
        minute -= (1 + distance)
    print(flow)
    print(path)

    #print(bfs_find_best_path("AA",0,1,set()))

        
        




p1()