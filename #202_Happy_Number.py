def isHappy(n):
    list = []
    b = n
    while n > 0:
        a = str(b)
        b = 0
        for i in range(len(a)):
            b += int(a[i]) * int(a[i])
        if b == 1 :
            return True
        elif b not in list:
           list.append(b)
        else:
            return False

print(isHappy(1))

