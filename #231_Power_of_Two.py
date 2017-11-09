def isPowerOfTwo(n):
    while n != 0:
        if n == 2:
            return True
        n = n / 2
    return False

def isPowerOfTwo_2(n):
    return n&n-1 == 0
