def maxCount(m,n,ops):
    list1 = []
    list2 = []
    for i in range(len(ops)):
        list1.append(ops[i][0])
        list2.append(ops[i][1])
    x = min(list1)
    y = min(list2)
    if x <= m and y <= n:
        return x*y
    elif x > m and y <= n:
        return m * y
    elif x <= m and y > n:
        return n * y
    else:
        return m * n
