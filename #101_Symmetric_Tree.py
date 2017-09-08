class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric_1(root):
    if not root:
        return True
    else:
        return isMirror(root.left,root.right)

def isMirror(p,q):
    if q and p:
        return True
    if q or p:
        return False
    return p.val == q.val and isMirror(p.left,q.right) and isMirror(p.right,q.left)

def isSymmetric_2(root):
    if root is None:
        return True
    stack = [(root.left,root.right)]
    while stack:
        left,right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.append((left.left,right.right))
            stack.append((left.right,right.left))
        else:
            return False
    return True








