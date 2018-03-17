def findLengthOfLCIS(nums):
    count = 1
    out = 1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            count +=1
        else:
            count = 1
        out = max(out,count)
    return 0 if len(nums) == 0 else out

