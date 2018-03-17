def validPalindrome_1(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
        left += 1
        right -= 1
    return True

def vaildPalindrome_2(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return help(left+1,right,s) or help(left,right-1,s)
        left += 1
        right -= 1
    return True

def help(l,r,s):
    while l<r:
        if s[r] !=s[l]:
            return False
        l += 1
        r -= 1
    return True
