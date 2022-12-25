# This doesnt work. No solution here...

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
    
    for line in read_input("day16/input.txt").splitlines():
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

def leastDistance(graph, source):
    Q = []

    distance = {k: 9999999 for k in graph}
    visited= set()
    Q.append(source)
    visited.update({0})
    while len(Q):
        vertex = Q.pop(0)
        if vertex == source:
            distance[vertex] = 0
        for u in graph[vertex]:
            if u not in visited:
                # update the distance
                if distance[u] > distance[vertex] + 1:
                    distance[u] = distance[vertex] + 1
                Q.append(u)
                visited.update({u})
    return distance




VALVES,RATES,EXITS = parse_input() #global
DISTANCES = {}
GOOD_VALVES = [v for v in VALVES if RATES[v] > 0]


for src in [*GOOD_VALVES,"AA"]:
    
    DISTANCES[src] = leastDistance(EXITS,src)


def dfs_highest_flow(start,minute,flow,open,path):
    if minute > 29:
        return [flow,path]
    
    flows = []

    next_valves = [v for v in GOOD_VALVES if v not in open]

    if ['KM', 'IC', 'OE', 'KT', 'AK', 'NK', 'NT'] == path:
        print("here")
        print(flow)
        print(minute)
    if len(next_valves) == 0:
        return [flow,path]

    paths = []
    

    for v in next_valves: #Valves to open
        new_open = deepcopy(open)
        new_open.add(v)
        minute_lapsed = minute + DISTANCES[start][v]+1
        new_flow = flow + (30-minute_lapsed)*RATES[v]
        score,p = dfs_highest_flow(v,minute_lapsed,new_flow,new_open,[*path,v])
        flows.append(score)
        paths.append(p)

    return [max(flows), paths[flows.index(max(flows))]]




def p1():
    start = "AA"
    open = set()

    
    #print(dfs_highest_flow(start,0,0,open,[]))
    

p1()