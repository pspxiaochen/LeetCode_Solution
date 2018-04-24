def countPrimeSetBits(L,R):
    res = 0
    for i in range(L,R+1):
        flag = True
        s = str(bin(i))
        count = s.count('1')
        if count == 1:
            continue
        for i in range(2,int(count**0.5)+1):
            if count % i == 0:
                flag = False
                break
        if flag:
            res += 1
    return res


def countPrimeSetBits_2(L,R):
    res = 0
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i in range(L,R+1):
        bits = 0
        while i > 0:
            bits += i & 1
            i >>= 1
        res +=  primes.count(bits)
    return res

