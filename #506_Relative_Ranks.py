def findRelativeRanks(nums):
    res = sorted(nums,reverse=True)
    count = 1
    for i in res:
        index = nums.index(i)
        if count == 1:
            nums[index] = "Gold Medal"
            count += 1
        elif count == 2:
            nums[index] = "Silver Medal"
            count += 1
        elif count == 3:
            nums[index] = "Bronze Medal"
            count += 1
        else:
            nums[index] = str(count)
            count += 1
    return nums

