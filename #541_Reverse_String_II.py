def reverseStr(s,k):
    if k > len(s):
        return s[::-1]
    a = ''
    m = 0
    n = k
    while n < len(s):
        a += s[m:n][::-1] + s[n:n + k]
        m += 2 * k
        n += 2 * k
    a += s[m:][::-1]
    return a

def reverseStr_2(s,k):
    i = 0
    while i < len(s):
        s = s[:i] + s[i:i+k][::-1] + s[i+k:]
        i += 2 * k
    return s
