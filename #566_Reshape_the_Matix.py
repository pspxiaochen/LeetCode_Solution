import numpy as np
def matrixReshape(nums,r,c):
    if r * c != len(nums) * len(nums[0]):
        return nums
    res = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            res.append(nums[i][j])
    count = 0
    out = []
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(res[count])
            count += 1
        out.append(temp)
    return out
