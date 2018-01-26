def arrayPairSum(nums):
    nums.sort()
    out = 0
    for i in range(0,len(nums),2):
        out += nums[i]
    return out

a = [1,4,3,2]