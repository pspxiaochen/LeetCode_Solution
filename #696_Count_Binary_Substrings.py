def countBinarySubstrings(s):
    res = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            res.append(count)
            count = 1
    res.append(count)
    out = 0
    for i in range(1,len(res)):
        out += min(int(res[i-1]),int(res[i]))
    return out

def countBinarySubstring_2(s):
    pre = 0
    cur = 1
    res = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cur += 1
        else:
            pre = cur
            cur = 1
        if pre >= cur:
            res += 1
    return res
