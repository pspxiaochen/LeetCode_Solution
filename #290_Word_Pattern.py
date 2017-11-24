def wordPattern(pattern,str):
    list = str.split(" ")
    if len(list) != len(pattern):
        return False
    dict = {}
    for i in range(len(pattern)):
        if pattern[i] not in dict.keys() and list[i] not in dict.values():
            dict[pattern[i]] = list[i]
        elif pattern[i] in dict.keys() and list[i] not in dict.values():
            return False
        elif pattern[i] not in dict.keys() and list[i] in dict.values():
            return False
        else:
            if dict[pattern[i]] != list[i]:
                return False
    return True

def wordPattern_2(pattern,str):
    list = str.split(" ")
    a = pattern
    return map(a.find, a) == map(list.index, list)
