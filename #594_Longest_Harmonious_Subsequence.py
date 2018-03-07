def findLHS(nums):
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = dict.get(nums[i],0) + 1
    result = 0
    for i in dict:
        if i+1 in dict:
            result = max(result,dict[i+1] + dict[i])
    return result

