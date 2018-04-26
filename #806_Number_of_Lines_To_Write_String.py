def numberOfLines(widths,S):
    count = 1
    line = 0
    for i in S:
        if line + widths[ord(i) - 97] <= 100:
            line += widths[ord(i) - 97]
        else:
            line = widths[ord(i) - 97]
            count += 1
    return [count,line]

