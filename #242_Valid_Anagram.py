def isAnagram(s,t):
    dict1 = {}
    dict2 = {}
    for i in s:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for j in t:
        if j not in dict2:
            dict2[j] = 1
        else:
            dict2[j] += 1
    for i in s:
        if i not in dict1 or i not in dict2:
            return False
        elif dict1[i] != dict2[i]:
            return False
    for j in t:
        if j not in dict1 or j not in dict2:
            return False
        elif dict1[j] != dict2[j]:
            return False
    return True

def isAnagram_2(s,t):
    if len(s) != len(t):
        return False
    dict = {}
    n = len(s)
    for i in range(n):
        if s[i] not in dict:
            dict[s[i]] = 0
        if t[i] not in dict:
            dict[t[i]] = 0
        dict[s[i]] += 1
        dict[t[i]] -= 1
    for i in dict:
        if dict[i]:
            return False
    return True

def isAnagram_3(s,t):
    if len(s) != len(t):
        return False
    a = [0] * 26
    for i in range(len(s)):
        a[ord(s[i])-ord('a')] += 1
        a[ord(t[i])-ord('a')] -= 1
    for i in a:
        if i != 0:
            return False
    return True


