def reverse_1(x):
    x = str(x)[::-1]
    maxint = 2**31
    if(x[len(x)-1]=='-'):
        x=0-int(x[0:len(x)-1])
    if not -maxint - 1 <=  int(x) <= maxint:
        x = 0
    return int(x)

######################
def reverse_2(x):
    s = (x>0) - (x<0)
    r = s*int(str(abs(x))[::-1])
    return r*(s*r<2**31)

######################
def reverse_3(x):
    rev = 0
    maxint = 2 ** 31
    while(x!=0):
        if(x<0):
            rev = rev*10 - int(abs(x)%10)
        else:
            rev = rev*10 + int(x%10)
        x = int(x / 10)
    if not -maxint - 1 <=  rev <= maxint:
        rev = 0
    return rev




