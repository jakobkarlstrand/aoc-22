def read_input(filepath):
    file = open(filepath, 'r')
    return file.readlines()
    
translate = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

# ROCK  1
# PAPER 2
# SCISSOR 3

# WIN 1 -> 2
# 2 -> 3
#3 -> 1


#LOSE 1 -> 3
# 2 -> 1 
# 3 -> 2



def get_points_from_round(opponent,me):
    opponent_t = translate[opponent]
    points = 0
    print(me)
    me_t = translate[me]

    print(opponent_t,me_t)
    
    if opponent_t - me_t == -1 or opponent_t-me_t == 2: # I WON
        points += 6 
    elif opponent_t == me_t: #DRAW
        points += 3
    else: # ELF WON
        pass
    points += me_t 
    return points



def get_points_from_round_part2(opponent,outcome):
    opponent_t = translate[opponent]
    points = 0

    outcome_t = translate[outcome]


    if outcome_t == 3: # I SHOULD WIN
        points += 6
        handPoints = 1 if opponent_t == 3 else opponent_t+1
        points += handPoints
    elif outcome_t == 2: #Draw
        points += 3
        points += opponent_t
    
    else: #Lose
        points += 3 if opponent_t == 1 else opponent_t-1

    
    return points

        

def part1():

    points = 0
    for line in read_input("day2/input.txt"):
        splitted = line.split(" ")
        [abc, xyz] = [splitted[0], splitted[1][0]]
        
        print(abc,xyz)

        points += get_points_from_round(abc,xyz)
    print(points)

def part2():

    points = 0
    for line in read_input("day2/input.txt"):
        splitted = line.split(" ")
        [abc, xyz] = [splitted[0], splitted[1][0]]
        
        print(abc,xyz)

        points += get_points_from_round_part2(abc,xyz)
    print(points)
part2()