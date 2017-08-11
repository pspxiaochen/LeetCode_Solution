from functools import reduce
def longestCommonPrefix_1(strs):
    if(len(strs) <= 0):
        return ""
    else:
        common_str = strs[0]
        i = 1
        while(i < len(strs)):
            if(strs[i][0:len(common_str)].find(common_str)!=-1):
                i += 1
            else:
                common_str = common_str[0:-1]
        return common_str

strs = ["","","","sdfas"]
print(len(strs))
print(longestCommonPrefix_1(strs))



def longestCommonPrefix_2(strs):
    if not strs:
        return ""
    else:
        l = 0
        for common_str in zip(*strs):
            if(len(set(common_str)) > 1):
                return strs[0][:l]
            l += 1
        return strs[0][:l]

class Solution:
    def lcp(self,str1,str2):
        i = 0
        while((i<len(str1))&(i<len(str2))):
            if(str1[i] == str2[i]):
                i += 1
            else:
                break
        return str1[:i]
    def longestCommonPrefix_3(self,strs):
        if not strs:
            return ""
        else:
            return reduce(self.lcp,strs)



