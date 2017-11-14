class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor_1(root,p,q):
    if (p.val >= root.val and q.val <= root.val) or (p.val <= root.val and q.val >= root.val):
        return root
    else:
        if (p.val > root.val):
            return lowestCommonAncestor_1(root.right,p,q)
        else:
            return lowestCommonAncestor_1(root.left,p,q)

def lowestCommonAncestor_2(root,p,q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = root.left if p.val < root.left else root.right
    return root