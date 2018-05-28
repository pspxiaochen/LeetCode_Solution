def divide(dividend,divisor):
    flag = False
    if ((dividend > 0 and divisor > 0 ) or (dividend < 0 and divisor < 0)):
        flag = True
    if dividend < 0:
        dividend = -dividend
    if divisor < 0:
        divisor = - divisor
    res = 0
    a = dividend
    b = divisor
    while a >= b:
        c = divisor
        i = 0
        while a >= c:
            a -= c
            res += 1 << i
            c <<= 1
            i += 1
    return res if flag == True else -res

