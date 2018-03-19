def calPoints(ops):
    output = 0
    roundList = []
    for i in ops:
        if i == '+':
            output += roundList[-1] + roundList[-2]
            roundList.append(roundList[-1] + roundList[-2])
        elif i == 'D':
            output += roundList[-1] * 2
            roundList.append(roundList[-1] * 2)
        elif i == 'C':
            output -= roundList[-1]
            roundList.pop()
        else:
            output += int(i)
            roundList.append(int(i))
    return output

