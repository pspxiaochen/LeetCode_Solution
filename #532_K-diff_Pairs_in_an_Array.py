def findPairs(nums,k):
    if k < 0:
        return 0
    count = 0
    a = list(set(nums))
    if k == 0:
        for i in list(set(nums)):
            if nums.count(i) > 1:
                count += 1
    else:
        for j in a:
            if j + k in a:
                count += 1
    return count

def findPairs_2(nums,k):
    if k < 0:
        return 0
    dict = {}
    count = 0
    for i in nums:
        dict[i] = dict.get(i,0) + 1
    if k == 0:
        for i in dict:
            if dict[i] >= 2:
                count += 1
    else:
        for i in dict:
            if i + k in dict:
                count += 1
    return count

