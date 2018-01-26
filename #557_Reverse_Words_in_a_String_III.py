def reverseWords(s):
    res = s.split()
    out = ''
    for i in res:
        out += i[::-1]
        out += ' '
    return out[:-1]
