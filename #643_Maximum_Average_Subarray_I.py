def findMaxAverage(nums,k):
    right = k
    sum_ = sum(nums[0:right])
    max_ = sum_
    while right <= len(nums):
        sum_ += nums[right] - nums[right - k]
        max_ = max(max_,sum_)
        right += 1
    return max_ / k

