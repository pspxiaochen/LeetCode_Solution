import math
def checkPerfectNumber(num):
    res = [1]
    for i in range(2,int(math.sqrt(num))+1,2):
        if num % i == 0:
            res.append(i)
            res.append(num / i)
    return sum(set(res)) == num

