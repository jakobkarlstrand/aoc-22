import math
from decimal import *
import collections
import re
from copy import deepcopy
from collections import OrderedDict

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


def parse_input():
    lines = read_input("day19/input.txt").splitlines()
    robot_costs = OrderedDict()
    ore_robot = OrderedDict()
    clay_robot = OrderedDict()
    obsidian_robot = OrderedDict()
    geode_robot = OrderedDict()

    for line in lines:
        blue,rest = line.split(":")
        id = int(blue.split("Blueprint ")[1])
        ore,clay,obsidian,geode,_ = rest.split(".")
        ore_cost = ore.split("costs ")[1]
        clay_cost = clay.split("costs ")[1]
        obsidian_cost = obsidian.split("costs ")[1]
        geode_cost = geode.split("costs ")[1]
        ore_cost = int(ore_cost.split(" ")[0])
        clay_cost = int(clay_cost.split(" ")[0])
        obsidian_cost_list = [int(obsidian_cost.split(" ore and ")[0])]
        obsidian_cost_list.append(int(obsidian_cost.split(" ore and ")[1].split(" ")[0]))
        geode_cost_list = [int(geode_cost.split(" ore and ")[0]),int(geode_cost.split(" ore and ")[1].split(" ")[0])]
        
        costs = OrderedDict()
        costs = {
            "ore": ore_cost,
            "clay": clay_cost,
            "obsidian": obsidian_cost_list,
            "geode": geode_cost_list
        }

        robot_costs[id] = costs

    return robot_costs
        
        

BLUEPRINTS = parse_input()

PRIO_LIST = ['geode', 'obsidian','clay','ore']

def can_build_robot(robot,blueprint,inventory):
    if robot == "ore":
        return inventory['ore'] >= blueprint['ore']
    if robot == "clay":
        return inventory['ore'] >= blueprint['clay']
    if robot == "obsidian":
        return inventory['ore'] >= blueprint['obsidian'][0] and inventory['clay'] >= blueprint['obsidian'][1]
    if robot == "geode":
        return inventory['ore'] >= blueprint['geode'][0] and inventory['obsidian'] >= blueprint['geode'][1]

    raise TypeError

def build_robot(robot,blueprint,inventory):
    if robot == "ore":
        inventory['ore'] = inventory['ore'] - blueprint['ore']
    elif robot == "clay":
        inventory['ore'] = inventory['ore'] - blueprint['clay']
    elif robot == "obsidian":
        inventory['ore'] = inventory['ore'] - blueprint['obsidian'][0]
        inventory['clay'] = inventory['clay'] - blueprint['obsidian'][1]
    elif robot == "geode":
        inventory['ore'] = inventory['ore'] - blueprint['geode'][0]
        inventory['obsidian'] = inventory['obsidian'] - blueprint['geode'][1]

SEEN = set()
def dfs(minute, inventory, robots,blueprint):
    if minute > 24:
        return inventory['geode']
    

    for material in robots: #Collect materials
        inventory[material] += robots[material]
    
    robot_built = False
    res = inventory['geode']

    seen_str = ""
    for i in inventory:
        seen_str += "_"
        seen_str += str(inventory[i])
    for i in robots:
        seen_str += "_"
        seen_str += str(robots[i])
    seen_str += "_"
    seen_str += str(minute)
    print(len(SEEN))
    if seen_str not in SEEN:
        SEEN.add(seen_str)
        for material in PRIO_LIST:
            if can_build_robot(material,blueprint,inventory):
                inv_copy = deepcopy(inventory)
                robots_copy = deepcopy(robots)

                build_robot(material,blueprint,inv_copy)
                robots_copy[material] += 1
                res = max(res,dfs(minute+1,inv_copy,robots_copy,blueprint))
        
    
    
    
    


    return max(res,dfs(minute+1,inventory,robots,blueprint))
    
    


    

def evaluate_blueprint(blueprint):
    minutes = 1
    inventory = {
        "ore" : 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
    }
    robots = {
        "ore" : 1,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
    }
    return (dfs(1,inventory,robots,blueprint))
    # while minutes <= 24:
    #     print(inventory)
    #     for material in PRIO_LIST:
    #         if can_build_robot(material,blueprint,inventory):
                
    #             build_robot(material,blueprint,inventory)
    #             print("built ", material)
    #             robots[material] += 1
    #             minutes += 1
    #             break

                
    #     for material in robots:
    #         inventory[material] += robots[material]

    #     minutes+=1
    
    # return inventory['geode']
    
    


def p1():
    answer = 0
    for id in (1,len(BLUEPRINTS)):
        print("ID",id)

        geodes = evaluate_blueprint(BLUEPRINTS[id])
        print(geodes)
        
        answer += geodes*id

    print(answer)

p1()