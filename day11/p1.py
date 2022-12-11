import math
from decimal import *

def read_input(filepath):
    file = open(filepath, 'r')
    return file.read()



raw = [lines.split("\n") for lines in read_input("day11/input.txt").split("\n\n")]

monkeys = []

for line in raw:
    monkey = {}
    items = line[1].split(": ")[1].split(", ")
    monkey['items'] = [int(item) for item in items ]

    operation = line[2].split("= ")[1]
    monkey['operation'] = operation

    test_divis = int(line[3].split("by ")[1])
    monkey['test'] = test_divis

    throw_if_true = int(line[4].split("monkey ")[1])
    throw_if_false = int(line[5].split("monkey ")[1])
    monkey['test_true'] = throw_if_true
    monkey['test_false'] = throw_if_false
    monkeys.append(monkey)

inspections = [0 for i in range(len(monkeys))]

mod = 1

for x in monkeys:
    mod *= x['test']


for c in range(10000):
    
    for monkey_idx in range(len(monkeys)):
        monkey = monkeys[monkey_idx]
        idx = 0
        count = 0
        while len(monkeys[monkey_idx]['items']) > 0:

            left,operator,right = monkey['operation'].split(" ")
            left = (monkey['items'][idx]) if left == "old" else int(left)
            right =(monkey['items'][idx]) if right == "old" else int(right)

            new_val = right + left if operator == "+" else left*right

            new_val %=  mod
       

            monkey['items'][idx] = new_val
    
            throw_true = new_val % monkey['test'] == 0
            
            throw_to_index = monkey['test_true'] if throw_true else monkey['test_false']
            item_to_throw = monkey['items'].pop(idx)
            monkeys[throw_to_index]['items'].append(item_to_throw)
     
            count += 1

        inspections[monkey_idx] += count
        

print(inspections.pop(inspections.index(max((inspections))))*max(inspections))






        



   
