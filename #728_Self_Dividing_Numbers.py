def selfDividingNumbers(left,right):
    res = []
    for i in range(left,right + 1):
        flag = True
        str_num = str(i)
        if '0' in str_num:
            continue
        for j in str_num:
            if i % int(j) != 0:
                flag = False
                break
        if flag:
            res.append(i)
    return res


def selfDividingNumbers_2(left,right):
    res = []
    for i in range(left,right + 1):
        flag = True
        j = i
        while j:
            d = j % 10
            if d == 0 or i % d != 0:
                flag = False
            j //= 10
        if flag:
            res.append(i)
    return res



