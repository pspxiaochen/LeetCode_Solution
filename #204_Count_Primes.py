def countPrimes_1(n):
    count = 0
    for i in range(2,n,1):
        if isPrime(i):
            count += 1
    return count
import math
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,math.trunc(math.sqrt(num)+1),1):
        if num % i == 0:
            return False
    return True



def countPrimes_2(n):
    count = 0
    used = [None] * n
    for i in range(2,n+1,1):
        if not used[i-1]:
            temp = i * i
            while temp < n:
                used[temp-1] = True
                temp += i
    for i in range(2,n,1):
        if not used[i-1]:
            count += 1
    return count

def countPrimes_3(n):
    used = [None] * n
    count = 0
    for i in range(2,n,1):
        if used[i] == None:
            count += 1
            j = 2
            while (i * j < n):
                used[i*j] = True
                j += 1
    return count

def countPrimes_4(n):
    if n <= 2:
        return 0
    used = [False, False] + [True] * (n - 2)
    for i in range(2,int(n ** 0.5)+1):
        if used[i]:
            used[i*i:n:i] = [False] * len(used[i*i:n:i])
    return sum(used)













