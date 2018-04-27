import re
def mostCommonWord(paragraph,banned):
    paragraph = [s.strip("!?',;.") for s in paragraph.lower().split(' ')]
    dict = {}
    for word in paragraph:
        if word in banned:
            continue
        else:
            dict[word] = dict.get(word,0) + 1
    Max = max(dict.values())
    return [k for k,v in dict.items() if v == Max][0]





