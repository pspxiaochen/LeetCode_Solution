def findDisappearedNumbers(nums):
    out = []
    for i in range(1,len(nums)+1):
        if i not in nums:
            out.append(i)
    return out

def findDisappearedNumbers_2(nums):
    res = []
    for i in range(len(nums)):
        val = abs(nums[i]) - 1
        if nums[val] > 0:
            nums[val] = -nums[val]
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i+1)
    return res

def findDisappearedNumbers_3(nums):
    res = [i not in nums for i in range(1,len(nums)+1)]
    out = []
    for i in range(len(res)):
        if res[i] == True:
           out.append(i+1)
    return out

def findDisappearedNumbers_4(nums):
    return list(set(i for i in range(1,len(nums)+1)) - set(nums))


