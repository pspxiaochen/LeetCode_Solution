def moveZeroes(nums):
    count = 0
    long = len(nums)
    while count < len(nums):
        if nums[count] == 0:
            del(nums[count])
        else:
            count += 1
    nums += (long-len(nums)) * [0]


def moveZeroes_2(nums):
    j = 0
    for i in nums:
        if i != 0:
            nums[j] = i
            j += 1
    while j < len(nums):
        nums[j] = 0
        j += 1

