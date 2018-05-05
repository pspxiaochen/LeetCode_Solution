def longestPalindrome(s):
    if len(s) == 0:
        return ""
    res = ""
    for i in range(2 * len(s) - 1):
        left = i // 2
        right = i // 2
        if i % 2 == 1:
            right += 1
        temp = helper(s,left,right)
        if len(res) < len(temp):
            res = temp
    return res

def helper(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left:right]
