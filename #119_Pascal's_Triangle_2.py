def getRow_1(rowIndex):
    list=[]
    if rowIndex < 0:
        return list
    for i in range(rowIndex+1):
        list.insert(0,1)
        for j in range(1,len(list)-1):
            list[j] = list[j] + list[j+1]
    return list

def getRow_2(rowIndex):
    res = [1]
    for i in range(rowIndex):
        res = list(map(lambda x, y: x + y, res + [0], [0] + res))
    return res
