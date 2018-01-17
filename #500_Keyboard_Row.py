def findWords(words):
    dict = {'Q':3,'W':3,'E':3,'R':3,'T':3,'Y':3,'U':3,'I':3,'O':3,'P':3,'A':2,'S':2,'D':2,'F':2,'G':2,'H':2,'J':2,'K':2,'L':2,'Z':1,'X':1,'C':1,'V':1,'B':1,'N':1,'M':1}
    res = []
    for i in range(len(words)):
        temp = []
        word = words[i].upper()
        for j in word:
            temp.append(dict[j])
        if len(set(temp)) == 1:
            res.append(words[i])
    return res

def findWords_2(words):
    line1 = set('QWERTYUIOP')
    line2 = set('ASDFGHJKL')
    line3 = set('ZXCVBNM')
    res = []
    for i in words:
        if set(i.upper()).issubset(line1) or set(i.upper()).issubset(line2) or set(i.upper()).issubset(line3):
            res.append(i)
    return res

