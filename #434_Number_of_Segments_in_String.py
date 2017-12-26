def countSegments(s):
    return len(s.split())

def countSegments_2(s):
    res = 0
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
            res += 1
    return res

