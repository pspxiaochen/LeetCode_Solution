def hammingWeight_1(n):
    count = 0
    while n:
        if n % 2 !=0:
            count+=1
        n=n>>1
    return count

def hammingWeight_2(n):
    count = 0
    while n:
        n &= (n-1)
        count += 1
    return count

