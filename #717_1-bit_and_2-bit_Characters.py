def isOneBitCharacter(bits):
    i = 0
    if len(bits) == 1:
        return True if bits[i] == 0 else False
    elif len(bits) == 2:
        return True if bits[i] == 0 else False
    else:
        while i <= len(bits)-3:
            if bits[i] == 1:
                i += 2
            elif bits[i] == 0:
                i += 1
        return True if bits[i] == 0 else False

def isOneBitCharacter_2(bits):
    i = 0
    while i < len(bits) - 1:
        if bits[i] == 0:
            i += 1
        else:
            i += 2
    return i == len(bits) - 1
