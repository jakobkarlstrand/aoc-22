import math
from decimal import *
import collections


def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


    


def parse_input():
    lines = read_input("day13/input.txt").split("\n\n")
    lists = []
    for pair in lines:
       
        left,right = pair.split("\n")
        lists.append((eval(left),eval(right)))
    return lists




def compare_lists(l1,l2):
    if not list in [type(l1), type(l2)]:
        d = (l2 - l1)
        return d/abs(d) if d != 0 else 0
    

    
    if type(l1) != list:
        l1 = [l1]
    if type(l2) != list:
        l2 =[l2]
    _idx = 0



    while _idx < len(l1) and _idx < len(l2):

        cmp = compare_lists(l1[_idx],l2[_idx])
        if cmp != 0:
            return cmp
        _idx+=1

    
    if len(l1) < len(l2): return 1
    if len(l1) > len(l2): return -1 
    
    return 0


        


    
def p1():
    input = parse_input()
    n_sorted = 0
    idx = 1

    for left,right in input:
        compare = compare_lists(left,right)
        
        if compare == 1:
            n_sorted+=idx
        
        idx += 1


    print("PART 1: ", n_sorted)

def p2():
    input = parse_input()
    divider_packets = [[[2]],[[6]]]

    all_packets = []
    for pair in input:
        all_packets += pair

    all_packets += divider_packets


    for i in range(len(all_packets)-1):
        for j in range(i,len(all_packets)):
            if compare_lists(all_packets[i], all_packets[j]) == -1:
                [all_packets[i],all_packets[j]] = [all_packets[j], all_packets[i]]
    
    signal = 1
    
    for i,packet in enumerate(all_packets):
        if packet in divider_packets:
            signal *= i
    

    print("PART 2: ", signal)
    
        
    
        

    
p1()
p2()