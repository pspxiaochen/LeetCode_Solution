def findNthDigit(n):
    s = ''
    for i in range(1,n+1,1):
        s += str(i)
        if n <= len(s):
            return int(s[n-1])

def findNthDigit_2(n):
    len = 1
    count = 9
    start = 1
    while ( n > len * count):
        n -= len * count
        len += 1
        count *= 10
        start *= 10
    start += (n - 1) // len
    s = str(start)
    return int(s[(n - 1) % len])



