def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    left = 0
    right = 1
    res = 0
    while right < len(s):
        if s[right] not in s[left:right]:
            right +=1
        else:
            tmp = right - left
            if res < tmp:
                res = tmp
            left += 1
    return max(right - left,res)


