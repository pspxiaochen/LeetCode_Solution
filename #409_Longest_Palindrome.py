def longestPalindrome(s):
    if len(set(s)) == 1:
        return len(s)
    array = [0] * 52
    for i in s:
        array[ord(i) - ord('a')] += 1
    sum = 0
    tem = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            sum += array[i]
        elif array[i] == 1 :
            tem = 1
        elif array[i] > 1:
            sum += array[i] - 1
            tem = 1
    return sum + tem

def longestPalindrome_2(s):
    if not s or len(s) == 0:
        return 0
    a = set()
    count = 0
    for i in s:
        if i in a:
            a.remove(i)
            count += 1
        else:
            a.add(i)
    if len(a) !=0:
        return count * 2 + 1
    return count * 2








