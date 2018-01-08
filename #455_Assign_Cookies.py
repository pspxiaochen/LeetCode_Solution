def findContentChildren(g,s):
    g=sorted(g)
    s=sorted(s)
    i = 0
    j = 0
    while (i < len(g)) and (j < len(s)):
        if g[i] <= s[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i

print(findContentChildren([10,9,8,7],[5,6,7,8]))