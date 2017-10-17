def trailingZeroes_1(n):
    if n ==0:
        return 0
    count = 0
    while(n!=0):
        count += n // 5
        n = n // 5
    return count

def trailingZeroes_2(n):
    return 0 if n == 0 else n//5 + trailingZeroes_2(n // 5)
