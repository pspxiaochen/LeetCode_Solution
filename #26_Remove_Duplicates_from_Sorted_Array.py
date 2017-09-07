def removeDuplicates_1(nums):
    if not nums:
        return 0
    else:
        count = 0
        for i in range(1,len(nums)):
            if(nums[i]!=nums[count]):
                count +=1
                nums[count] = nums[i]
    return count+1

