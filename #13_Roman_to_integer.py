def romanToInt_1(s):
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    out = 0
    i=1
    if(len(s)==1):
        return dict[s]
    while(i<len(s)):
        if(dict[s[i]]>dict[s[i-1]]):
            out += dict[s[i]] - dict[s[i-1]]
            i += 2
        else:
            out += dict[s[i-1]]
            i += 1
    if(dict[s[-1]]>dict[s[-2]]):
        return out
    else:
        return out+dict[s[-1]]

def romanToInt_2(s):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    out = 0
    for i in range(len(s)-1):
        if (dict[s[i]]<dict[s[i+1]]):
            out -= dict[s[i]]
        else:
            out += dict[s[i]]
    return out + dict[s[-1]]
