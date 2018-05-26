def generateParenthesis(n):
    res= []
    help(n,n,'',res)
    print(res)

def help(left,right,item,res):
    if right < left:
        return
    if left == 0 and right == 0:
        res.append(item)
    if left > 0:
        help(left - 1,right,item + '(',res)
    if right > 0 :
        help(left,right - 1,item + ')',res)
