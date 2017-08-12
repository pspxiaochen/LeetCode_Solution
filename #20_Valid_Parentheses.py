def isValid_1(s):
    dict = {'(':1,'[':2,'{':3,')':4,']':5,'}':6}
    i = 0
    while(i<len(s)):
        if((s[i] in dict) & (len(s)%2 == 0)):
            if(dict[s[i]]<=3):
                i += 1
            else:
                if(dict[s[i]]-dict[s[i-1]] ==3):
                    s = s[:i-1] + s[i+1:]
                    i = i - 1
                else:
                    return False
        else:
            return False
    return (len(s) == 0)

def isValid_2(s):
    dict = {"]": "[", "}": "{", ")": "("}
    stack = []
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if(stack == [] or dict[char]!=stack.pop()):
                return False
        else:
            return False
    return stack == []

def isValid_3(s):
    stack = []
    for char in s:
        if char == '{':
            stack.append('}')
        elif char =='(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif stack == [] or stack.pop()!= char:
            return False
    return stack == []
