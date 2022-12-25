import math
from decimal import *
from collections import deque, Counter
import re
from copy import deepcopy
from collections import defaultdict

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()

def parse_input():
    lines = read_input("day25/input.txt").splitlines()
    return lines


def snafu_to_decimal(snafu):
    decimal = 0
    for i,char in enumerate(snafu):
        pos = len(snafu)-i-1
        snafu_num = 0
        if char == "-":
            snafu_num = -1
        elif char == "=":
            snafu_num = -2
        else:
            snafu_num = int(char)
        decimal += snafu_num*5**pos
    return decimal

def dfs(rest,snafu_str, pos):

    if rest == 0:
        print(pos)
        if pos == -1:

            return snafu_str
        else:
            
            return snafu_str + "0"
    
    
    if pos < 0:
        return ""


    digits = [2,1,0,-1,-2]
    digits_rest = []

    for dig in digits:
        diff = abs(rest - dig*5**pos)
        digits_rest.append((diff,dig))
    digits_rest.sort()


    


    for top3 in digits_rest:
        char = top3[1]
        if char == -2:
            char = "="
        elif char == -1:
            char = "-"
        test = dfs(rest-top3[1]*5**pos,snafu_str+str(char),pos-1)
        if test != "":
            return test
    
    return ""




def start_digit_and_rest(num):


    digits = [2,1,0,-1,-2]
    
    best_match = (0,0) # Digit, pos
    rest = num

    closest = num+1
    
    for pos in range(1,len(str(abs(rest)))*2):
        
        for digit in digits:
            diff = abs((rest)-(digit * 5**pos))
            
            if diff < closest:
                closest = diff
                best_match = (digit,pos)
    


    
    rest = num - best_match[0]*5**best_match[1]

    return rest,best_match[1],best_match[0]
    



        


def p1():
    SNAFU = parse_input()

    
    

    total = 0
    
    for number in SNAFU:
        decimal = snafu_to_decimal(number)
        total += decimal
        

    
    rest,pos,dig = start_digit_and_rest(total)

    snafu_str = dfs(rest,str(dig),pos-1)
    
    print(snafu_str)
    snafu_decimal_from_str = snafu_to_decimal(snafu_str)


    

    
    assert snafu_decimal_from_str == total

    print("ANSWER P1: ", snafu_str)


p1()