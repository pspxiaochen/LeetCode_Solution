import collections
def canConstruct(ransomNote,magazine):
    dict = {}
    for i in ransomNote:
        dict[i] = dict.get(i, 0) + 1
    for j in ransomNote:
        if dict[j] > magazine.count(j):
            return False
    return True

def canConstruct_2(ransomNote,magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)

def canConstruct_3(ransomNote,magazine):
    arr = [0] * 26
    for i in range(len(magazine)):
        arr[ord(magazine[i]) - ord('a')] += 1
    for j in range(len(ransomNote)):
        arr[ord(ransomNote[j])-ord('a')] -= 1
        if arr[ord(ransomNote[j])-ord('a')] < 0:
            return False
    return True

