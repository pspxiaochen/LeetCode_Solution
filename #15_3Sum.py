def threeSum(nums):
    res = set()
    if len(nums) < 3:
        return res
    nums = sorted(nums)
    for i in range(len(nums)):
        list = [nums[i]]
        left = i+1
        right = len(nums) - 1
        tar = -nums[i]
        while left < right:
            if nums[left] + nums[right] == tar:
                list.append(nums[left])
                list.append(nums[right])
                res.add(list)
                list = [nums[i]]
                left += 1
                right -= 1
            elif nums[left] + nums[right] > tar:
                right -= 1
            else:
                left += 1
    return res
