class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def findTarget(root,k):
    res = []
    res = help(root,res)
    dict = {}
    for i in res:
        if (k - i) in dict:
            return True
        else:
            dict[i] = k - i
    return False

def help(root,res):
    res.append(root.val)
    if root.left:
        help(root.left,res)
    if root.right:
        help(root.right,res)
    return res

def findTarget_2(root,k):
    node = [root]
    s = set()
    for i in node:
        if k - i.val in s:
            return True
        s.add(i.val)
        if i.left:
            node.append(i.left)
        if i.right:
            node.append(i.right)
    return False


