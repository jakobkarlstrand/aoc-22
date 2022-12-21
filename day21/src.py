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
    lines = read_input("day21/input.txt").splitlines()
    monkeys = dict()
    root = None
    for line in lines:
        name, operation = line.split(": ")
        monkey = {}

        
        try:
            num = int(operation)
            monkey['operation'] = num
            monkey['done'] = True
        except:
            monkey['operation'] = operation
            monkey['done'] = False

        if name == "root":
            root = monkey
        else:
            monkeys[name] = monkey
    return root,monkeys


def p1():
    root,monkeys = parse_input()
    
    l_root,_,r_root = root['operation'].split(" ")
    answer = 0
        
    while True:

        
        if monkeys[l_root]['done'] and monkeys[r_root]['done']:
            l_val = monkeys[l_root]['operation']
            r_val = monkeys[r_root]['operation']
            answer = l_val + r_val
            break
            

        for name in monkeys:
            if not monkeys[name]['done']:
                l_name,op,r_name = monkeys[name]['operation'].split(" ")

                if monkeys[l_name]['done'] and monkeys[r_name]['done']:
                    if op == "+":
                        monkeys[name]['operation']  = monkeys[l_name]['operation'] + monkeys[r_name]['operation']
                    elif op == "-":
                        monkeys[name]['operation']  = monkeys[l_name]['operation'] - monkeys[r_name]['operation']
                    elif op == "*":
                        monkeys[name]['operation']  = monkeys[l_name]['operation'] * monkeys[r_name]['operation']
                    elif op == "/":
                        monkeys[name]['operation'] = monkeys[l_name]['operation'] // monkeys[r_name]['operation']
                    monkeys[name]['done'] = True
            

    print("ANSWER P1: ",answer)
    return answer

                        
def p2():
    root,monkeys = parse_input()
    was_negative = False
    
    
    MAX_GUESS = p1()
    found = False
    h_low,h_mid,h_high = 0,MAX_GUESS//2, MAX_GUESS
    
    l_root,_,r_root = root['operation'].split(" ")
    while not found:
        copy_monkeys = deepcopy(monkeys)
        copy_monkeys['humn']['operation'] = h_mid
        
        
    
        

        
        while True:

            
            if copy_monkeys[l_root]['done'] and copy_monkeys[r_root]['done']:
                l_val = copy_monkeys[l_root]['operation']
                r_val = copy_monkeys[r_root]['operation']

                if l_val < 0 or was_negative:
                    was_negative = True
                    [l_val,r_val] = [r_val,l_val]

                diff = l_val - r_val
                if l_val == r_val:
                    found = True

                elif diff > 0:
                    h_low = h_low
                    h_high = h_mid
                    h_mid = h_mid - ((h_mid-h_low) // 2)+1
                

                    
                else:
                    h_low = h_mid
                    h_mid = h_mid + (h_high-h_mid)//2
                    h_high = h_high
                break
                
            
            for name in copy_monkeys:
                if not copy_monkeys[name]['done']:
                    l_name,op,r_name = copy_monkeys[name]['operation'].split(" ")

                    if copy_monkeys[l_name]['done'] and copy_monkeys[r_name]['done']:
                        if op == "+":
                            copy_monkeys[name]['operation']  = copy_monkeys[l_name]['operation'] + copy_monkeys[r_name]['operation']
                        elif op == "-":
                            copy_monkeys[name]['operation']  = copy_monkeys[l_name]['operation'] - copy_monkeys[r_name]['operation']
                        elif op == "*":
                            copy_monkeys[name]['operation']  = copy_monkeys[l_name]['operation'] * copy_monkeys[r_name]['operation']
                        elif op == "/":
                            copy_monkeys[name]['operation'] = copy_monkeys[l_name]['operation'] // copy_monkeys[r_name]['operation']
                        copy_monkeys[name]['done'] = True
                
    #print(monkeys['root']['operation'])
    
    print("ANSWER P2: ",h_mid)

p1()
p2()
