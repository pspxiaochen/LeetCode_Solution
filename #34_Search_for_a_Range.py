def searchRange(nums,target):
    l = -1
    r = -1
    if len(nums) == 0:
        return [l,r]
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while(left < right):
        if nums[mid] == target:
            break
        elif nums[mid] > target:
            right = mid - 1
            mid = (left + right) // 2
        else:
            left = mid + 1
            mid = (left + right) // 2
    if nums[mid] == target :
        l = mid
        r = mid
        while (l-1 >=0 and nums[l-1] == target):
            l -= 1
        while (r+1 <= len(nums) -1 and nums[r+1] == target):
            r += 1
    return [l,r]

