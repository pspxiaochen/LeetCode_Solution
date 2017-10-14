def majorityElement_1(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] =1
    return (max(dict,key=dict.get))

def majorityElement_2(nums):
    major = nums[0]
    count = 1
    for i in range(1,len(nums)):
        if count == 0:
            count += 1
            major = nums[i]
        elif major == nums[i]:
            count += 1
        else:
            count -= 1
    return major

def majorityElement_3(nums):
    if len(nums) == 1:
        return nums[0]
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
            if dict[i] > len(nums) / 2:
                return i
        else:
            dict[i] = 1