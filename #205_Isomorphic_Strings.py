def isIsomorphic_1(s,t):
    if len(set(s)) != len(set(t)):
        return False
    dict = {}
    for i in range(len(s)):
        dict[s[i]] = t[i]
    for i in range(len(s)):
        if dict[s[i]] != t[i]:
            return False
    return True

def isIsomorphic_2(s,t):
    return len(set(zip(s,t))) == len(set(s)) == len(set(t))

def isIsomorphic_3(s,t):
    return [s.find(i) for i in s] == [t.find(j) for j in t]
