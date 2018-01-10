def repeatedSubstringPattern(s):
    a = (s+s)[1:-1]
    return a.find(s) != -1

def repeatedSubstringPattern_2(s):
    for i in range(len(s)//2,0,-1):
        tmp = ''
        if len(s) % i != 0:
            continue
        else:
            for j in range(len(s)//i):
                tmp += s[:i]
            if tmp == s:
                return True
    return False



