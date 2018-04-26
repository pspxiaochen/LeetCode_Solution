def rotateDigits(N):
    res = 0
    a = ['2','5','6','9']
    b = ['3','4','7']
    for i in range(N+1):
        flag = False
        Str = str(i)
        for j in Str:
            if j in b:
                flag = False
                break
            if j in a:
                flag = True
        if flag:
            res += 1
    return res
