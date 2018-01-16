def findMaxConsecutiveOnes(nums):
    if 1 not in nums:
        return 0
    if len(nums) == 1:
        return 1 if nums[0] == 1 else 0
    count = 1
    max = 1
    for i in range(1,len(nums),1):
        if nums[i] == nums[i-1] == 1:
            count += 1
        else:
            count = 1
        if count > max:
            max = count
    return max

def findMaxConsecutiveOnes_2(nums):
    count = 0
    max_ = 0
    for i in nums:
        count = 0 if i == 0 else count + 1
        max_ = max(max_,count)
    return max_
