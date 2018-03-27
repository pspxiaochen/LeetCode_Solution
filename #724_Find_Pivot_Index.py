def pivotIndex(nums):
    if len(nums) == 0:
        return -1
    sum_ = sum(nums)
    count = 0
    for i in range(len(nums)):
        if sum_ - count - nums[i] == count:
            return i
        else:
            count += nums[i]
    return -1
