def numJewelsInStones(J,S):
    res = 0
    for i in J:
        res += S.count(i)
    return res
