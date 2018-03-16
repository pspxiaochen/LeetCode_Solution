class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# 递归写法
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

# 非递归写法

def trimBST_2(root,L,R):
    if not root:
        return root
    while root.val < L or root.val > R:
        if root.val < L:
            root = root.right
        if root.val > R:
            root = root.left

    dummy = root
    while dummy:
        while dummy.left and dummy.left.val < L:
            dummy.left = dummy.left.right
        dummy = dummy.left

    dummy = root
    while dummy:
        while dummy.right and dummy.right.val > R:
            dummy.right = dummy.right .left
        dummy = dummy.right
    return root