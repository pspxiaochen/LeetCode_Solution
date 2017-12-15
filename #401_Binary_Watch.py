def bitcount(n):
    count = 0
    while n > 0:
        if (n & 1 == 1): count += 1
        n >>= 1
    return count
def readBinaryWatch(num):
    list = []
    for i in range(12):
        for j in range(60):
            if bitcount(i*64+j) == num:
                list.append('%d:%02d' % (i, j))
    return list

#-----------------------------------------------------------------------------
def readBinaryWatch_2(num):
    hour = [[0],[1,2,4,8],[3,5,6,9,10],[7,11]]
    minutes = [[0],[1,2,4,8,16,32],[3,5,6,9,10,12,17,18,20,24,33,34,36,40,48],
        [7,11,13,14,19,21,22,25,26,28,35,37,38,41,42,44,49,50,52,56],
        [15,54,23,27,29,30,39,51,43,45,46,57,58,53],[31,47,55,59]]
    list = []
    boundary = 4 if num >= 4 else num+1
    for i in range(boundary):
        index = num - i
        if index > 5:
            continue
        for j in range(len(hour[i])):
            for k in range(len(minutes[index])):
                if (minutes[index][k]<10):
                    minute = '0'+str(minutes[index][k])
                else:
                    minute = str(minutes[index][k])
                temp = str(hour[i][j])+':'+minute
                list.append(temp)
    return list

#---------------------------------------------------------------------
def readBinaryWatch_3(num):
    res = []
    nums1 = [8,4,2,1]
    nums2 = [32,16,8,4,2,1]
    for i in range(num+1):
        list1 = generateDigit(nums1,i)
        list2 = generateDigit(nums2,num-i)
        for num1 in list1:
            if num1 >= 12:
                continue
            for num2 in list2:
                if num2 >= 60:
                    continue
                res.append(str(num1) + ':' + (str(num2) if num2> 10 else '0'+ str(num2)))
    return res

def generateDigit(nums,count):
    res = []
    generateDigitHelper(nums,count,0,0,res)
    return res

def generateDigitHelper(nums,count,pos,sum,res):
    if count == 0:
        res.append(sum)
        return
    for i in range(pos,len(nums),1):
        generateDigitHelper(nums,count - 1,i + 1,sum + nums[i],res)

print(readBinaryWatch_3(2))

