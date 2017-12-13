def findTheDifference(s,t):
    for i in t:
        if s.count(i)!=t.count(i):
            return i

def findTheDifference_2(s,t):
    c = 0
    for i in s:
        c ^= ord(i)
    for i in t:
        c ^= ord(i)
    return chr(c)

