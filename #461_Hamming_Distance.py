def hammingDistance(x,y):
    a = x ^ y
    count = 0
    while (a > 0):
        if a & 1==1:
            count += 1
        a=a >> 1
    return count

def hammingDistance_2(x,y):
    return bin(x^y).count('1')