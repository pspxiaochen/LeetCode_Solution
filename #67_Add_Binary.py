def addBinary_1(a,b):
    a_ = 0
    b_ = 0
    for i in range(len(a)):
        a_ += int(a[i]) * (2**(len(a)-i-1))
    for j in range(len(b)):
        b_ += int(b[j]) * (2**(len(b)-j-1))
    sum = bin(a_+b_).replace('0b','')
    return (sum)
