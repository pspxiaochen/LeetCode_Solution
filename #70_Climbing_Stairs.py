<<<<<<< HEAD
def climbStairs_1(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    return climbStairs_1(n-1) + climbStairs_1(n-2)

def climbStairs_2(n):
    if n==1:
        return 1
    if n==2:
        return 2
    f1=1
    f2=2
    for i in range(3,n+1):
        f3 = f1+f2
        f1 = f2
        f2 = f3
    return f2

def climbStairs_3(n):
    a = b =1
    for i in range(n):
        a,b=b,a+b
    return a
=======
def climbStairs_1(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    return climbStairs_1(n-1) + climbStairs_1(n-2)

def climbStairs_2(n):
    if n==1:
        return 1
    if n==2:
        return 2
    f1=1
    f2=2
    for i in range(3,n+1):
        f3 = f1+f2
        f1 = f2
        f2 = f3
    return f2

def climbStairs_3(n):
    a = b =1
    for i in range(n):
        a,b=b,a+b
    return a
>>>>>>> f591eb1c08fb1fdb158d747d63451b73e2f00dbd
