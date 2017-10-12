def twoSum_1(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i]+numbers[j] == target):
                return sorted([i+1,j+1])


def twoSum_2(numbers,target):
    dict = {}
    for i in range(len(numbers)):
        if numbers[i] in dict:
            return sorted([dict[numbers[i]],i])
        else:
            dict[target-numbers[i]] = i

def twoSum_3(numbers,target):
    r = [0,0]
    left = 0
    right = len(numbers)-1
    while(left<right):
        v = numbers[left] + numbers[right]
        if v == target:
            r[0] = left + 1
            r[1] = right + 1
            break
        elif v < target:
            left += 1
        else:
            right -= 1
    return r

def twoSum_4(numbers,target):
    for i in range(len(numbers)):
        l,r=i+1,len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = (l+r)//2
            if numbers[mid] == tmp:
                return [i+1,mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid -1

print(twoSum_4([2,3,4,10],14))