def rob_1(nums):
    if not nums:
        return 0
    dict = {}
    for i in range(len(nums)):
        if i == 0:
            dict[i] = nums[0]
        elif i == 1:
            dict[i] = max(nums[0],nums[1])
        else:
            dict[i] = max(dict[i-1],dict[i-2]+nums[i])
    return dict[len(nums)-1]

def rob_2(nums):
    a = 0
    b = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            a = max(a+nums[i],b)
        else:
            b = max(b+nums[i],a)
    return max(a,b)
