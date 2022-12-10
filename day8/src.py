def read_input(filepath):
    file = open(filepath, 'r')
    return file.read().splitlines()



def part1():
    rows = read_input("day8/input.txt")

    grid = [[*s] for s in rows]



    def isVisible(x0,y0, grid, height):
        visible = [True,True,True,True]
        xTemp = x0+1

        while xTemp < len(grid[0]):
            if int(grid[y0][xTemp]) >= height:
                visible[0] = False
            xTemp += 1
        
        xTemp = x0-1
        while xTemp >= 0 and xTemp < len(grid[0]):
            if int(grid[y0][xTemp]) >= height:
                visible[1] = False
            xTemp -= 1

        yTemp = y0+1
        
        while yTemp < len(grid):
            if int(grid[yTemp][x0]) >= height:
                visible[2] = False
            yTemp += 1
        
        yTemp = y0-1
        while yTemp >= 0 and yTemp < len(grid):
            if int(grid[yTemp][x0]) >= height:
                visible[3] = False
            yTemp -= 1

        return True in visible

    visible_trees = 0

    for y in range(1,len(grid)-1):
        for x in range(1,len(grid[0])-1):
            visible_trees += 1 if isVisible(x,y,grid,int(grid[y][x])) else 0


    edges = len(grid[0])*2 + 2*(len(grid)-2)
    print("PART1: ", visible_trees + edges)





def part2():
    rows = read_input("day8/input.txt")

    grid = [[*s] for s in rows]



    def get_scenic_score(x0,y0, grid, height):

        scores = [0,0,0,0]
        xTemp = x0+1

        while xTemp < len(grid[0]):
            if int(grid[y0][xTemp]) < height:
                scores[0] += 1
            else:
                scores[0] += 1
                break
            xTemp += 1
        
        xTemp = x0-1
        while xTemp >= 0 and xTemp < len(grid[0]):
            if int(grid[y0][xTemp]) < height:
                scores[1] += 1
            else:
                scores[1] += 1
                break
            xTemp -= 1
        

        yTemp = y0+1
        
        while yTemp < len(grid):
            if int(grid[yTemp][x0]) < height:
                scores[2] +=1
            else:
                scores[2] += 1
                break
            yTemp += 1
        
        yTemp = y0-1
        while yTemp >= 0 and yTemp < len(grid):
            if int(grid[yTemp][x0]) < height:
                scores[3] += 1

            else:
                scores[3] += 1
                break
            yTemp -= 1

        product = 1

        for score in scores:
            product *= score
        return product

    max_score = 0

    for y in range(1,len(grid)-1):
        for x in range(1,len(grid[0])-1):
            current_score = get_scenic_score(x,y,grid,int(grid[y][x]))

            max_score = max(max_score, current_score)



    print("PART2: ", max_score)

part1()
part2()
