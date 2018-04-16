def floodFill(image,sr,sc,newColor):
    SR, SC = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor: return image
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1: dfs(r - 1, c)
            if r < SR - 1: dfs(r + 1, c)
            if c >= 1: dfs(r, c - 1)
            if c < SC - 1: dfs(r, c + 1)
    dfs(sr, sc)
    return image

