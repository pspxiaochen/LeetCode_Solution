def repeatedStringMatch(A,B):
    count = 1
    if B in A:
        return count
    tmp = A
    while len(tmp) <= 2*len(B):
        tmp += A
        count += 1
        if B in tmp:
            return count
    return -1 if B not in A else count


def repeatedStringMatch_2(A,B):
    tmp = A
    count = 1
    while len(tmp) < len(B):
        tmp += A
        count += 1
    if B in tmp:
        return count
    if B in tmp+A:
        return count + 1
    return -1

