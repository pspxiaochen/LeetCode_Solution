def lengthOfLastWord_1(s):
    if not s:
        return 0
    count = 0
    i = -1
    while(len(s)+i>=0 and s[i]==" "):
        i -= 1
    if(-i-1==len(s)):
        return 0
    for j in range(len(s)+i,-1,-1):
        if(s[j]==" "):
            break
        else:
            count += 1
    return count

def lengthOfLastWord_2(s):
    count = 0
    length = len(s) - 1
    while((length>=0) and (s[length]== " ")):
        length -= 1
    while((length>=0) and (s[length])!=" "):
        count += 1
        length -= 1
    return count

s = "hello world"
print(lengthOfLastWord_2(s))