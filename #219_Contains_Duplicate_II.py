def containsNearbyDuplicate_1(nums,k):
    for i in range(len(nums)):
        for j in range(i+1,len(nums),1):
            if nums[i] == nums[j] and abs(i-j)<=k:
                return True
    return False

def containsNearbyDuplicate_2(nums,k):
    appearNum = set()
    start = 0
    end = 0
    for i in range(len(nums)):
        if nums[i] not in appearNum:
            appearNum.add(nums[i])
            end += 1
        else:return True
        if end - start>k:
            appearNum.remove(nums[start])
            start += 1
    return False

def containsNearbyDuplicate_3(nums,k):
    dict = {}
    for i in range(len(nums)):
        if nums[i] not in dict.keys():
            dict[nums[i]] = i
        else:
            if i-dict[nums[i]] > k:
                dict[nums[i]] = i
            else:return True
    return False

def containsNearbyDuplicate_4(nums,k):
    a = set()
    for i in range(len(nums)):
        if i > k:
            a.remove(nums[i-k-1])
        if nums[i] in a:
            return True
        else:
            a.add(nums[i])
    return False



