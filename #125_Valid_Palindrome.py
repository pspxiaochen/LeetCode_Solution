def isPalindrome_1(s):
    i = 0
    j = len(s)-1
    while i < j:
        print(i < j and not s[i].isalnum())
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower()!=s[j].lower():
                return False
        i += 1
        j -= 1
    return True

def isPalindrome_2(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
    return True

def isPalindrome_3(s):
    s = "".join([c.lower() for c in s if c.isalnum()])
    return s == s[::-1]