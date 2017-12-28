def findAnagrams(s,p):
    out = []
    dict1 = {}
    for i in p:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for i in range(len(s)-len(p)+1):
        count = 0
        dict2 = {}
        tmp = s[i:i+len(p)]
        if len(set(p)) != len(set(tmp)):
            continue
        for j in tmp:
            if j not in dict2:
                dict2[j] =1
            else:
                dict2[j] += 1
        for j in tmp:
            if j not in dict1:
                break
            if dict1[j] != dict2[j]:
                break
            else:
                count += 1
            if count == len(dict1):
                out.append(i)
    return out

def findAnagrams_2(s,p):
    out = []
    if s == None or len(s) == 0 or p == None or len(p) == 0:
        return out
    hash = [0] * 26
    for i in p:
        hash [ord(i) - ord('a')] += 1
    left = 0
    right = 0
    count = len(p)
    while(right < len(s)):
        if (hash[ord(s[right])- ord('a')] >= 1):
            count -= 1
        hash[ord(s[right])- ord('a')] -= 1
        right += 1
        if count == 0:
            out .append(left)

        if (right - left == len(p)):
            if hash[ord(s[left])- ord('a')] >= 0:
                count += 1
            hash[ord(s[left])- ord('a')] += 1
            left +=1
    return out

print(findAnagrams_2('ababa','ghgd'))


