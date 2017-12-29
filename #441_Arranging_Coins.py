def arrangeCoins(n):
    sum = 0
    count = 0
    while sum < n:
        count += 1
        sum += count
    if sum == n :
        return count
    else:
        return count - 1
import math
def arrangeCoins_2(n):
    return int(math.sqrt(2*n+0.25) - 0.5)

