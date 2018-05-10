def threeSumClosest(nums,target):
    nums = sorted(nums)
    min = 999
    res = 0
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            Sum = nums[i] + nums[left] + nums[right]
            temp = target - Sum
            if abs(temp) < abs(min):
                min = temp
                res = Sum
            if target > Sum:
                left += 1
            else:
                right -= 1
    return res
