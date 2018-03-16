class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def trimBST(root,L,R):
    if not root:
        return root
    if root.val < L:
        return trimBST(root.right,L,R)
    elif root.val > R:
        return trimBST(root.left,L,R)
    else:
        root.left = trimBST(root.left,L,R)
        root.right = trimBST(root.right,L,R)
        return root
