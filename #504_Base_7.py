def convertToBase7(num):
    if num == 0:
        return '0'
    res = ''
    n = abs(num)
    while n !=0:
        res = str(n % 7) + res
        n //= 7
    return res if num > 0 else '-' + res

