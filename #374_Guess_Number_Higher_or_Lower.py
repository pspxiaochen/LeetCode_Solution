def guess(nums):
    pass
def guessNumber(n):
    low = 1
    high = n
    while(low<high):
        mid = (low + high) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            high = mid - 1
        elif guess(mid) == 1:
            low = mid + 1
    return low
