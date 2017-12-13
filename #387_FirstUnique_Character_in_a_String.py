def firstUniqChar(s):
    dict = {}
    for i in s:
        dict[i] = dict.get(i, 0) + 1
    for j in range(len(s)):
        if dict[s[j]] == 1:
            return j
    return -1

def firstUniqChar_2(s):
    a = [0] * 26
    for i in s:
        a[ord(i) - ord('a')] += 1
    for j in range(len(s)):
        if a[ord(s[j]) - ord('a')] == 1:
            return j
    return - 1

def firstUniqChar_3(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    index = [s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index)>0 else -1

