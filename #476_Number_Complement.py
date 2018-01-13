def findComplement(num):
    num = bin(num)
    a = ''
    for i in str(num)[2:]:
        a += str(1-int(i))
    return int(a,2)

def findComplement_2(num):
    i = 1
    while i <= num:
        i = i<<1
    print(i)
#最高位1前面的肯定都是1了，这一部分跟上面得到的掩码相与，肯定是0，不需要考虑了。剩下的部分取反后与掩码相与正好保留下来。符合题目要求。
