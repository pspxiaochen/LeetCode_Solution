import math
def isPerfectSquare(num):
    crr = num
    while(crr * crr > num):
        crr = (crr + num / crr) // 2
    if int(crr) * int(crr) == num:
        return True
    return False


