def isBadVersion(version):
    if version == 1:
        return False
    else :
        return True

def firstBadVersion(n):
    low = 1
    high = n
    while(low < high):
        mid = (high + low) // 2
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

print(firstBadVersion(2))


