import math
from decimal import *
import collections


def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()


def parse_input():
    lines = read_input("day15/input.txt").splitlines()
    sensors_n_beacons = []
    for line in lines:
        div = line.split(":")
        sensor = div[0][9:].split(",")
        beacon = div[1][22:].split(",")

        beacon_coor = (int(beacon[0].strip().replace("x=","")),int(beacon[1].strip().replace("y=","")))
        sensor_coor = (int(sensor[0].strip().replace("x=","")),int(sensor[1].strip().replace("y=","")))
        item = {
            "beacon" : beacon_coor,
            "sensor" : sensor_coor,
        }

        sensors_n_beacons.append(item)
    return sensors_n_beacons
def p1():
    S_B = parse_input()

    Y = 10


    impossible_ranges = []
    occupied = set()

    impossible_ranges = analyze_row(S_B,float("inf"),Y,limit=False)
    for sb in S_B:
        if sb['beacon'][1] == Y:
            occupied.add(sb['beacon'][0])
    print(impossible_ranges)
    merged_ranges = merge_ranges(impossible_ranges)

    

    print(merged_ranges)

    n_impossible = abs(merged_ranges[0][1]-merged_ranges[0][0]) - len(occupied)+1
    

    
    print("ANSWER PART 1: ", n_impossible)
             


def analyze_row(all_beacons_and_sensors, MAX_XY,Y,limit=True):
    impossible_ranges = []


    for item in all_beacons_and_sensors:
        (bx,by),(sx,sy) = item['beacon'],item['sensor']
        
        dist = abs(sx-bx) + abs(sy-by) # Manhattan

        offset = dist - abs(sy-Y)

        if offset < 0:
            continue

        lx,hx = sx - offset, sx+offset
        if limit: # Only needed for part 2
            lx = max(0,lx)
            hx = min(hx,MAX_XY)

        impossible_ranges.append((lx,hx))
    

    return impossible_ranges


def merge_ranges(ranges):
    merged_ranges = []
    for start,end in sorted(ranges):

        if len(merged_ranges) == 0:
            merged_ranges.append([start,end])
            continue

        _,q_end = merged_ranges[-1]

        if start > q_end:
            merged_ranges.append([start,q_end])
            continue

        merged_ranges[-1][1] = max(q_end,end)


    
    return merged_ranges

def p2():
    S_B = parse_input()

    MAX_XY = 20

    signal = None

    idx_left = MAX_XY // 2
    idx_right = MAX_XY // 2 + 1
    signal = None
    y = 0
    while idx_left >= 0 and idx_left <= MAX_XY: # Start from middle, since prompt says it was close to Y = 2_000_000
        if signal is not None:
            break

        for i in [idx_left,idx_right]:
            ranges = analyze_row(S_B,MAX_XY, i)
            
            merged_ranges = merge_ranges(ranges)
            if len(merged_ranges) > 1:
                signal = merged_ranges
                y = i
                break
        
        idx_right += 1
        idx_left -= 1
        

        
    
    
    freq = (signal[1][0]-signal[0][0]-1)*4_000_000 + y

    print("ANSWER PART 2: ", freq)
p1()    
p2()
