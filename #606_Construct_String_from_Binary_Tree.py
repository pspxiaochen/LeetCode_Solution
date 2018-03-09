class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def tree2str(t):
    if t is None:
        return ""
    res = str(t.val)
    if t.left:
        res += "(" + tree2str(t.left) + ")"
        if t.right:
            res += "(" + tree2str(t.right) + ")"
    elif t.right:
        res += "()" + "(" + tree2str(t.right) + ")"
    return res


