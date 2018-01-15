import collections
def licenseKeyFormatting(S,K):
    if len(S) <= K:
        return S.upper()
    queue = collections.deque()
    S = S.upper()
    for i in S:
        if i != '-':
            queue.append(i)
    out = ''
    for i in range(len(queue) % K):
        out += queue.popleft()
    if len(out) != 0 :
        out += '-'
    i = 0
    while len(queue) != 0:
        if i != K:
            out += queue.popleft()
            i += 1
        else:
            i = 0
            out += '-'
    return out

def licenseKeyFormatting_2(s,k):
    res = ""
    for i in range(len(s)-1,-1,-1):
        if s[i] != '-':
            if len(res) % (k+1) != k:
                res += s[i]
            else:
                res += '-'
                res += s[i]
    return res[::-1].upper()

def licenseKeyFormatting_3(s,k):
    s = s.upper().replace('-', '')
    s1 = k if len(s)%k == 0 else len(s) % k
    res = s[:s1]
    while s1 < len(s):
        res += '-'+s[s1:s1+k]
        s1 += k
    return res
