def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i

def missingNumber_2(nums):
    for i in range(len(nums)):
        if i not in nums:
            return i
    return len(nums)

def missingNumber_3(nums):
    sum = len(nums)
    for i in range(len(nums)):
        sum += i - nums[i]
    return sum

def missingNumber_4(nums):
    n = len(nums)
    return n*(n+1)/2 - sum(nums)

def missingNumber_5(nums):
    n = len(nums)
    for i in range(n):
        n = n ^ i ^ nums[i]
    return n