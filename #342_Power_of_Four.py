import math
def isPowerOfFour(num):
    return num > 0 and (math.sqrt(num)) % 2 == 0 and 1073741824 % num == 0
