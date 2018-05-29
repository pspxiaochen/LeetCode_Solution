# *首先要明白: 什么是next
# permutation.简单点说, 如果输入的数字有大小的话, 那么
# next
# permutation就是下一个大于它并
# "最接近"
# 它的全排列.
# *比如123, 下一个使用
# 这三个数字的排列就是132(213, 312
# 虽然也是全排列, 但是都比132大)
# *如果这个全排列已经是最大的了(全部升序排列), 那么它的next
# permutation就来一个
# "头尾想接"(就是最小的数字):
# *比如321的排列已经是最大的了， 所以next
# permutation
# 就是把321完全反转成最小的123
def nextPermutation(nums):
    i = len(nums) - 2
    while (i >= 0 and nums[i] >= nums[i + 1]):
        i -= 1
    if i < 0:
        nums[:] = nums[::-1]
    else:
        max = 9999
        a = 0
        for s in range(i+1,len(nums)):
            if nums[s] - nums[i] <= max and nums[s] - nums[i] > 0:
                max = nums[s] - nums[i]
                a = s
        nums[i],nums[a] = nums[a],nums[i]
        nums[i+1:] = nums[i+1:][::-1]

