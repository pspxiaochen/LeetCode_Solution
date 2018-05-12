def letterCombinations(digits):
    dict = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
    res = [""]
    if digits == None or len(digits) == 0:
        return []
    for i in range(len(digits)):
        s = dict[digits[i]]
        newR = []
        for j in range(len(res)):
            for k in range(len(s)):
                newR.append(res[j] + s[k])
        res = newR
    return res

def letterCombinations_2(digits):
    def help(digits,c,res):
        if not digits:
            res.append(c)
            return
        for i in dict[digits[0]]:
            help(digits[1:],c+i,res)

    dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    res = []
    help(digits,'',res)
    return res


