class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees(t1,t2):
    if t1 and t2:
        ans = TreeNode(t1.val + t2.val)
        ans.left = mergeTrees(t1.left,t2.left)
        ans.right = mergeTrees(t1.right,t2.right)
        return ans
    else:
        return t1 or t2