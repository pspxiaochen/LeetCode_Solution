def searchInsert_1(nums,target):
    i = 0
    while(i<len(nums)):
        if nums[i] < target:
            i += 1
        else:
            return i
    return i

def searchInsert_2(nums,target):
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = int((low + high)/2)
        if(nums[mid] == target):
            return mid
        elif(nums[mid] > target):
            high = mid -1
        elif(nums[mid] < target):
            low = mid + 1
    return low

def searchInsert_3(nums,target):
    return len([x for x in nums if x<=target])
