def maxAreaOfIsland(grid):
    max = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            island = dfs(grid,i,j)
            if island > max:
                max = island
    return max

def dfs(grid,i,j):
    if 0<=i<=len(grid)-1 and 0<=j<=len(grid[0])-1 and grid[i][j]:
        grid[i][j] = 0
        return 1 + dfs(grid,i-1,j) + dfs(grid,i+1,j) + dfs(grid,i,j-1) + dfs(grid,i,j+1)
    return 0
