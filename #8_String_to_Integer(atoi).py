from itertools import takewhile
def myAtoi(self, s):
    s = s.lstrip()
    sign = list(takewhile(lambda ch: ch in set("+-"), s))
    if len(sign) > 1:
        return 0

    digits = list(takewhile(lambda ch: ch in set("1234567890"), s[len(sign):]))
    try:
        r = int("".join(sign) + "".join(digits))
    except ValueError:
        return 0
    return max(min(r, 2 ** 31 - 1), -2 ** 31)