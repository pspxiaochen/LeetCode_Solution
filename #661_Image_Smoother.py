def imageSmoother(M):
    c = len(M)
    r = len(M[0])
    ans = [[0 for i in range(r)] for i in range(c)]
    for i in range(c):
        for j in range(r):
            count = 0
            for x in range(i - 1,i + 2):
                for y in range(j - 1,j + 2):
                    if x>=0 and x < c and y>=0 and y<r:
                        count += 1
                        ans[i][j] += M[x][y]
            ans[i][j] //= count
    return ans

