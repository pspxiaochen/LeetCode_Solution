def isPowerOfThree(n):
    if n == 0:
        return False
    while n % 3 == 0:
        n /= 3
    if n == 1:
        return True
    return False

def isPowerOfThree_2(n):
    return n > 0 and 1162261467 % n == 0