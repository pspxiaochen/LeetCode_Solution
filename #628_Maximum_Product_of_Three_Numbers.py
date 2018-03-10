def maximumProduct(nums):
    nums = sorted(nums)
    out1 = nums[-1] * nums[-2] * nums[-3]
    out2 = nums[0] * nums[1] * nums[-1]
    return out1 if out1 > out2 else out2

def maximumProduct_2(nums):
    max1 = -2**31
    max2 = -2**31
    max3 = -2**31
    min1 = 2**31
    min2 = 2**31
    for i in nums:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2:
            max3 = max2
            max2 = i
        elif i > max3:
            max3 = i
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
    return max(max1*max2*max3,min1*min2*max1)
