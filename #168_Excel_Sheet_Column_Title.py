def convertToTitle(n):
    return "" if n == 0 else convertToTitle((n - 1)//26)+chr((n - 1) % 26 + ord('A'))

print(convertToTitle(111))