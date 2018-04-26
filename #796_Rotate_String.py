def rotateString(A,B):
    if len(A) == 0 and len(B) == 0:
        return True
    if len(A)!=len(B):
        return False
    i = 0
    while i < len(A):
        A = A[1:] + A[0]
        if A == B:
            return True
        else:
            i += 1
    return False

def rotateString_2(A,B):
    if len(A)!=len(B):
        return False
    S = A + A
    if B in S:
        return True
    else:
        return False