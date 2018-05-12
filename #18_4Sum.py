def fourSum(nums,target):
    res = []
    nums = sorted(nums)
    for i in range(len(nums) - 3):
        for j in range(i+1,len(nums) - 2):
            left = j + 1
            right = len(nums) - 1
            while(left < right):
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    if [nums[i],nums[j],nums[left],nums[right]] not in res:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif target - nums[i] - nums[j] > nums[left] + nums[right]:
                    left += 1
                else:
                    right -= 1
    return res

def fourSum_2(nums,target):
    dict = {}
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            s = nums[i] + nums[j]
            if s in dict:
                dict[s].append([i,j])
            else:
                dict[s] = [(i,j)]

    res = set()
    for key in dict:
        value = target - key
        if value in dict:
            list1 = dict[key]
            list2 = dict[value]
            for (i,j) in list1:
                for (k,l) in list2:
                    if i!=k and i!=l and j!=k and j!=l:
                        l = [nums[i],nums[j],nums[k],nums[l]]
                        l.sort()
                        res.add(tuple(l))
    return list(res)

print(fourSum_2([1, 0, -1, 0, -2, 2],0))
