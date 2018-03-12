def findErrorNums(nums):
    list = []
    dis = 0
    n = len(nums)
    sum = (n+1)*n / 2
    for i in nums:
        if i in list:
            dis = i
        sum -= i
        list.append(i)
    return [dis,sum+dis]


def findErrorNums_2(nums):
    count = [0] * len(nums)
    for i in nums:
        count[i-1] += 1
    for i in range(len(count)):
        if count[i] == 2:
            two = i+1
        elif count[i] == 0:
            never = i+1
    return [two , never]
