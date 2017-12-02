def reverseVowels(s):
    if not s and len(s) == 0:
        return s
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    start = 0
    end = len(s) - 1
    s = list(s)
    while start < end:
        while(start < end and s[start] not in vowels):
            start += 1
        while(start < end and s[end] not in vowels):
            end -= 1
        s[start],s[end] = s[end],s[start]
        start += 1
        end -= 1
    return ''.join(s)
import re
def reverseVowels_1(s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


