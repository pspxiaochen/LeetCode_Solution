def mySqrt_1(x):
    crr = x
    while(crr*crr>x):
        crr = (crr + x /crr) / 2
    return int(crr)

def mySqrt_2(x):
    left,right = 0,x
    while(left<=right):
        mid = (right+left) // 2
        if(mid*mid<=x<(mid+1)*(mid+1)):
            return mid
        elif mid*mid>x:
            right = mid -1
        else:
            left = mid + 1

