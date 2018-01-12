def islandPerimeter(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0:
                    count += 1
                if j == 0:
                    count += 1
                if i == len(grid) - 1:
                    count += 1
                if j == len(grid[i]) -1:
                    count += 1
                if i != 0:
                    if grid[i-1][j] != 1:
                        count += 1
                if i != len(grid)-1:
                    if grid[i+1][j] != 1:
                        count += 1
                if j != 0:
                    if grid[i][j-1] != 1:
                        count += 1
                if j != len(grid[i]) - 1:
                    if grid[i][j+1] != 1:
                        count += 1
    return count

def islandPerimeter_2(grid):
    island = 0
    n = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                island += 1
                if i<len(grid) - 1 and grid[i+1][j] == 1:
                    n += 1
                if j<len(grid[i]) - 1 and grid[i][j+1] == 1:
                    n += 1
    return island * 4 - n * 2



