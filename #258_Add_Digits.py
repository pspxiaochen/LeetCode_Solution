def addDigits(num):
    if num<10:
        return num
    num_str = str(num)
    while len(num_str) != 1:
        count = 0
        for i in range(len(num_str)):
            count += int(num_str[i])
        num_str = str(count)
    return int(num_str)

def addDigits_2(num):
    if num ==0 :
        return 0
    return 1+(num-1)%9