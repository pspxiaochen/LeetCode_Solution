def toHex(num):
    if num < 0:
        num = 4294967296 + num
    if num == 0:
        return '0'
    out = ''
    dict = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    while num != 0:
        tmp = num % 16
        if tmp > 9:
            out += dict[tmp]
        else:
            out += str(tmp)
        num = num // 16
    return out[::-1]

def toHex_2(num):
    if num < 0:
        num = 4294967296 + num
    list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    if num == 0:
        return '0'
    out = ''
    while num !=0:
        out += list[(num & 15 )]
        num = num >> 4
    return out[::-1]
