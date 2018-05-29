def search(nums,target):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while left <= right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[right]:
            if nums[mid] < target and target <= nums[right] :
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        elif nums[mid] >= nums[right]:
            if nums[mid] > target and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
    return -1