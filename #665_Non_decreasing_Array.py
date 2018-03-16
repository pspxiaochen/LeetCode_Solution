def checkPossibility(nums):
    count = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            count += 1
            if i -2 <0 or nums[i] >= nums[i-2]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
        if count == 2:
            return False
    return True


