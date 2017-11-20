def isUgly(num):
    if num == 0:
        return True
    elif num == 1:
        return False
    elif num % 2 == 0:
        return isUgly(num / 2)
    elif num % 3 == 0:
        return isUgly(num / 3)
    elif num % 5 == 0:
        return isUgly(num / 5)

def isUgly_1(num):
    for i in 2,3,5:
        while num % i == 0 < num:
            num /= i
        return num == 1
