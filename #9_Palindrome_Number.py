#class Solution(object):
def isPalindrome_1(x):
    return (str(x) == str(x)[::-1])

########################################

def isPalindrome_2(x):
        if((x<0)|((x!=0)&(x%10==0))):
            return False
        rev = 0
        while(x>rev):
            rev = rev * 10 + x%10
            x = x / 10
        return ((rev == x) | (x == rev / 10))
