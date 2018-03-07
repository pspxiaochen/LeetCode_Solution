def findUnsortedSubArray(nums):
    if sorted(nums) == nums:
        return 0
    while len(nums)!=0 and min(nums) == nums[0]:
        nums.pop(0)
    while len(nums)!=0 and max(nums) == nums[-1]:
        nums.pop(-1)
    return len(nums)

def findUnsortedSubarray_2(nums):
    n = len(nums)
    end = -2
    beg = -1
    biggest = nums[0]
    smallest = nums[-1]
    for i in range(1,len(nums)):
        biggest = max(biggest,nums[i])
        smallest = min(smallest,nums[n-i-1])
        if nums[i] < biggest:
            end = i
        if nums[n-i-1] > smallest:
            beg = n-i-1
    return end - beg + 1

