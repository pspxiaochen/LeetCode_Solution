def convert(s,numRows):
    if s == None or len(s) <= 1 or numRows <= 1:
        return s
    res = ""
    list = []
    idx = 0
    down = True
    for i in range(numRows):
        list.append("")
    for i in range(len(s)):
        list[idx] += s[i]
        if (idx == numRows - 1):
            down = False
        elif (idx==0):
            down = True
        if down:
            idx +=1
        else:
            idx -=1
    for i in range(numRows):
        res += list[i]
    return res

print(convert("PAYPALISHIRING",4))