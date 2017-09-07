<<<<<<< HEAD
def countAndSay(n):
    if (n == 1):
        return '1'
    s = str(countAndSay(n-1)) + '*'
    count = 1
    temp = ""
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            count += 1
        else:
            temp = temp + str(count) + s[i]
            count = 1
    return temp

=======
def countAndSay(n):
    if (n == 1):
        return '1'
    s = str(countAndSay(n-1)) + '*'
    count = 1
    temp = ""
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            count += 1
        else:
            temp = temp + str(count) + s[i]
            count = 1
    return temp

>>>>>>> f591eb1c08fb1fdb158d747d63451b73e2f00dbd
