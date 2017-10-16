def titleToNumber_1(s):
    count = 0
    for i in range(len(s)):
        count += (ord(s[i])-64) * 26**(len(s)-1-i)
    return count
from functools import reduce
def titleToNumber_2(s):
    return reduce(lambda x,y:26*x+y,[ord(i) - 64 for i in s])

