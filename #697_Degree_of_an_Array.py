
def findShortestSubArray(nums):
    set_nums = set(nums)
    if len(nums) == len(set_nums):
        return 1
    maxList = []
    temp = 0
    out = 999999
    for i in set_nums:
        if nums.count(i)>temp:
            temp = nums.count(i)
            maxList = []
            maxList.append(i)
        elif nums.count(i) == temp:
            maxList.append(i)
    while maxList:
        num = maxList.pop()
        if len(nums)-nums[::-1].index(num) -nums.index(num) < out:
            out = len(nums) - nums[::-1].index(num) -nums.index(num)
    return out

def findShortestSubArray_2(nums):
    dict1 = {}
    dict2 = {}
    degree = 0
    minSize = len(nums)
    for i in range(len(nums)):
        dict1[nums[i]] = dict1.get(nums[i],0) + 1
        degree = max(degree,dict1[nums[i]])
        if nums[i] not in dict2:
            dict2[nums[i]] = [None] * 2
        numRange = dict2[nums[i]]
        if numRange[0] == None:
            numRange[0] = i
        numRange[1] = i
    for i in dict1:
        if dict1[i] != degree:
            continue
        range_ = dict2[i]
        minSize = min(minSize,range_ [1] - range_ [0] + 1)
    return minSize


