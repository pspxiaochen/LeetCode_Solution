def dominantIndex(nums):
    if len(nums) == 1:
        return 0
    index = nums.index(max(nums))
    a = nums.pop(index)
    return index if a >= max(nums) * 2 else -1

def dominantIndex_2(nums):
    if len(nums) == 1:
        return 0
    Max = 0
    secordMax = 0
    index = 0
    for i in range(len(nums)):
        if nums[i] > Max:
            secordMax = Max
            Max = nums[i]
            index = i
            continue
        if nums[i] > secordMax:
            secordMax = nums[i]
    if Max >= secordMax * 2:
        return index
    else:
        return -1

