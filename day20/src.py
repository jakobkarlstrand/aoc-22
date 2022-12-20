import math
from decimal import *
import collections
import re
from copy import deepcopy
from collections import defaultdict

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()

def get_sorted_dict_as_list(dict_numbers):
    number_list = []
    for idx in dict_numbers:
        item = (dict_numbers[idx]['new_index'], dict_numbers[idx]['num'])
        number_list.append(item)

    st = []
    for item in sorted(number_list):
        st.append(item[1])
    return st



def calc_circular_loop_index(idx,n_to_move,length):

    move_to = idx + n_to_move
    MAX_IDX = length-1
    if move_to > MAX_IDX:
            diff =  move_to - MAX_IDX
        
            move_to = diff % (MAX_IDX)


    elif move_to < 0: 
    
        diff = MAX_IDX-abs(move_to)
        
        move_to = diff % MAX_IDX
    return move_to


def solve(ORDER,number_dict):

    for i,n in enumerate(ORDER):
    
        current_num = number_dict[i]['num']
        if current_num == 0:
            continue
        
        move_to = calc_circular_loop_index(number_dict[i]['new_index'],current_num,len(ORDER))
        
    
        if number_dict[i]['new_index'] < move_to:

            for idx in number_dict:
                current_new_index = number_dict[idx]['new_index']
                if idx == i:
                    continue
                if current_new_index <= move_to and current_new_index > number_dict[i]['new_index']:
                    number_dict[idx]['new_index'] -= 1
                    
            number_dict[i]['new_index'] = move_to
        else: # 1 2 3 4 5 6 7
            for idx in number_dict:
                current_new_index = number_dict[idx]['new_index']
                if idx == i:
                    continue
                if current_new_index >= move_to and current_new_index < number_dict[i]['new_index']:
                    number_dict[idx]['new_index'] += 1
                    
            number_dict[i]['new_index'] = move_to




def p1():
    lines = read_input("day20/input.txt").splitlines()
    lines = [int(line) for line in lines]
    
    dict_numbers = dict()
    for i,line in enumerate(lines):
        item = {"num": line, "new_index": i}
        dict_numbers[i] = item

    solve(lines,dict_numbers)
    sorted_list = get_sorted_dict_as_list(dict_numbers)
    

    idx_0 = sorted_list.index(0)
    length = len(sorted_list)
    sum = 0
    for thousand in [1000,2000,3000]:
        sum += sorted_list[calc_circular_loop_index(idx_0,thousand,length+1)]
    print("ANSWER P1: ",sum)

def p2():
    lines = read_input("day20/input.txt").splitlines()
    multiplier = 811589153
    lines = [int(line)*multiplier for line in lines]
    
    dict_numbers = dict()
    for i,line in enumerate(lines):
        item = {"num": line, "new_index": i}
        dict_numbers[i] = item

    for id in range(10):
        print(str(id+1), "/ 10 Done...")
        solve(lines,dict_numbers) #Updates dict_numbers each time


    sorted_list = get_sorted_dict_as_list(dict_numbers)
    
    idx_0 = sorted_list.index(0)
    length = len(sorted_list)
    sum = 0
    for thousand in [1000,2000,3000]:
        sum += sorted_list[calc_circular_loop_index(idx_0,thousand,length+1)]
    print("ANSWER P2: ", sum)
    

p1()
p2()
