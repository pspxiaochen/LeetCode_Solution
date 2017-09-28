def singleNumber_1(nums):
    if len(nums) == 1:
        return nums[0]
    dict ={}
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for key,value in dict.items():
        if value == 1:
            return key

def singleNumber_2(nums):
    result = 0
    for i in nums:
        result = result ^ i
    return result

def singleNumber_3(nums):
    return 2*sum(set(nums)) - sum(nums)
