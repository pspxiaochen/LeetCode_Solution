def hasAlternatingBits(n):
    tmp = str(bin(n))[2:]
    for i in range(len(tmp)-1):
        if tmp[i]==tmp[i+1]:
            return False
    return True

