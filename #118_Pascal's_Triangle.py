def generate_1(numRows):
    list = []
    if numRows <= 0:
        return list
    for i in range(numRows):
        list1 = []
        for j in range(i+1):
            if (j==1 or j==i):
                list1.append(1)
            else:
                list1.append(list[i-1][j-1]+list[i-1][j])
        list.append(list1)
    return list

def generate_2(numRows):
    res = [[1]]
    for i in range(1,numRows):
        res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
    return res if numRows>0 else []

print(generate_2(3))