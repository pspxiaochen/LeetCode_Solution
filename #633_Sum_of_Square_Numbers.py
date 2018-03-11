def judgeSquareSum(c):
    left = 0
    right = int(c ** 0.5)
    while left <= right:
        cur = left ** 2 + right ** 2
        if cur == c:
            return True
        elif cur < c:
            left += 1
        else:
            right -= 1
    return False

