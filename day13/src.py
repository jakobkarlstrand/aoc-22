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
        left_list = eval(left)
        right_list = eval(right)
        lists.append((left_list,right_list))
    return lists


# [[1],[2,3,4]]
# [[1],4]


def compare_lists(l1,l2):
    if type(l1) != list and type(l2) != list:
        if l1 > l2:
            return -1
        elif l2 > l1:
            return 1
        else:
            return 0

    if type(l1) != list:
        l1 = [l1]
    if type(l2) != list:
        l2 = [l2]
    _idx = 0



    while _idx < len(l1) and _idx < len(l2):

        if type(l1[_idx]) == list or type(l2[_idx]) == list:
            cmp = compare_lists(l1[_idx],l2[_idx])
            if cmp == -1:
                return -1
            elif cmp == 1:
                return 1
            else:
                _idx+=1
                continue
 
        if abs(l1[_idx] - l2[_idx]) != 0:

            return 1 if l1[_idx] < l2[_idx] else  -1
        
        
        _idx+=1
    
    if len(l1) < len(l2): return 1
    if len(l1) > len(l2): return -1 
    
    return 0


        


    
def p1():
    input = parse_input()
    n_sorted = 0
    idx = 1

    for pair in input:

    
        compare = compare_lists(pair[0],pair[1])
        
        if compare == 1:
            n_sorted+=idx
        
        idx += 1


    print("PART 1: ", n_sorted)

def p2():
    input = parse_input()
    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    all_packets = []
    for left,right in input:
        all_packets.append(left)
        all_packets.append(right)
    all_packets.append(divider_packet1)
    all_packets.append(divider_packet2)
    
    idx = 1

    for i in range(len(all_packets)-1):
        for j in range(i,len(all_packets)):
            if compare_lists(all_packets[i], all_packets[j]) == -1:
                temp = all_packets[j]
                all_packets[j] = all_packets[i]
                all_packets[i] = temp
    signal = 1
    idx = 1
    for packet in all_packets:
        if packet == divider_packet1 or packet == divider_packet2:
            signal *= idx
        idx += 1

    print("PART 2: ", signal)
    
        
    
        

    
p1()
p2()