def longestWord(words):
    words = sorted(words)
    res = ""
    built = []
    for i in words:
        if len(i) == 1 or i[:-1] in built:
            res = i if len(i) > len(res) else res
            built.append(i)
    return res
