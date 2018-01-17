def nextGreaterElement(findNums,nums):
    res = []
    for i in findNums:
        if i in nums:
            index = nums.index(i) + 1
            if index == len(nums):
                res.append(-1)
            while index <= len(nums) - 1:
                if nums[index] > i:
                    res.append(nums[index])
                    break
                else:
                    index += 1
                if index == len(nums)  :
                    res.append(-1)
                    break
    return res

def nextGreaterElement_2(findNums,nums):
    stack = []
    dict = {}
    for i in nums:
        while len(stack)!=0 and stack[-1] < i:
            dict[stack.pop()] = i
        stack.append(i)
    for i in range(len(findNums)):
        findNums[i] = dict.get(findNums[i],-1)
    return findNums

