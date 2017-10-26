def isHappy_1(n):
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
def isHappy_2(n):
    list = []
    while n not in list:
        list.append(n)
        squareSum = 0
        while n > 0:
            remain = n % 10
            squareSum += remain * remain
            n //= 10
        if squareSum == 1:
            return True
        else:
            n = squareSum
    return False

def isHappy_3(n):
    mem = set()
    while n != 1:
        n = sum([int(i) **2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
    return True



