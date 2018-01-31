class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def isSubtree(s,t):
    if s == None:
        return False
    if isEqual(s,t):
        return True
    else :
        return isSubtree(s.left,t) or isSubtree(s.right,t)
def isEqual(s,t):
    if s == None and t == None:
        return True
    elif s != None and t!=None:
        return s.val == t.val and isEqual(s.left,t.left) and isEqual(s.right,t.right)
    else:
        return False
