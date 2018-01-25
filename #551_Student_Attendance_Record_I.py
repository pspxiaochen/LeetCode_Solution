def checkRecord(s):
    if s.count('A') >= 2:
        return False
    for i in range(2,len(s)):
        if s[i-2] == s[i-1] == s[i] == 'L':
            return False
    return True

def checkRecord_2(s):
    a = 0
    l = 0
    for i in s:
        if i == 'A':
            a += 1
        if i == 'L':
            l += 1
        else:
            l = 0
        if l >2 or a >= 2:
            return False
    return True