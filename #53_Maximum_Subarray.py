<<<<<<< HEAD
def maxSubArray_1(nums):
    if not nums:
        return 0
    else:
        k = maxnum =nums[0]
        for num in nums[1:]:
            k = max(num,k+num)
            maxnum = max(maxnum,k)
        return maxnum


def maxSubArray_2(nums):
    dp=nums
    dp[0] = nums[0]
    maxnum = dp[0]
    for i in range(1,len(nums)):
        dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
        maxnum = max(maxnum,dp[i])
    return maxnum

=======
def maxSubArray_1(nums):
    if not nums:
        return 0
    else:
        k = maxnum =nums[0]
        for num in nums[1:]:
            k = max(num,k+num)
            maxnum = max(maxnum,k)
        return maxnum


def maxSubArray_2(nums):
    dp=nums
    dp[0] = nums[0]
    maxnum = dp[0]
    for i in range(1,len(nums)):
        dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
        maxnum = max(maxnum,dp[i])
    return maxnum

>>>>>>> f591eb1c08fb1fdb158d747d63451b73e2f00dbd
print(maxSubArray_2([-2,1,-3,4,-1,2,1,-5,4]))