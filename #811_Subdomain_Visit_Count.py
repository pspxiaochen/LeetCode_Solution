def subdomainVisits(cpdomains):
    dict = {}
    for word in cpdomains:
        a = word.split(" ")
        dict[a[1]] = dict.get(a[1],0) + int(a[0])
        for j in range(len(a[1])):
            if a[1][j] != '.':
                continue
            else:
                s = a[1][j+1:]
                dict[s] = dict.get(s,0) + int(a[0])
    res = []
    for i in dict:
        res.append("" + str(dict[i]) + " " + i)
    return res




