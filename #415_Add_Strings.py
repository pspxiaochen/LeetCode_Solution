def addStrings(num1,num2):
    long = len(num1) - len(num2)
    if long < 0:
        long = long * -1
    a = '0' * long
    if len(num1) > len(num2):
        num2 = a + num2
    else:
        num1 = a + num1
    sum = 0
    power = 0
    for i in range(len(num1)):
        sum += (int(num1[::-1][i]) + int(num2[::-1][i])) * (10 ** power)
        power += 1
    return str(sum)

def addStrings_2(num1,num2):
    i = len(num1) - 1
    j = len(num2) - 1
    res = ''
    carry = 0
    while i >= 0 or j >= 0 or carry > 0:
        sum = 0
        if i >= 0:
            sum += ord(num1[i]) - ord('0')
            i -= 1
        if j >= 0 :
            sum += ord(num2[j]) - ord('0')
            j -= 1
        sum += carry
        carry = sum // 10
        sum %= 10
        res = str(sum)+ res
    return res


