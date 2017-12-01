def reverseString(s):
    return s[::-1]

def reverseString_2(s):
    str = ''
    long = len(s) - 1
    while long != -1:
        str += s[long]
        long -= 1
    return str

def reverseString_3(s):
    return ''.join(s[i] for i in range(len(s) - 1, -1, -1))
