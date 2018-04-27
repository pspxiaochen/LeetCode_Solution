def shortestToChar(S,C):
    flag= []
    res = []
    for i in range(len(S)):
        if S[i] == C:
            flag.append(i)
    for i in range(len(S)):
        distances = [abs(dist - i) for dist in flag]
        res.append(min(distances))
    return res
