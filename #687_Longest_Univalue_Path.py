class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def longestUniValuePath(root):
    if not root:
        return 0
    res = 0
    if root.left and root.left.val == root.val:
        res = 1 + dfs(root.left)
    if root.right and root.right.val == root.val:
        res += 1 + dfs(root.right)
    return (max(res,longestUniValuePath(root.left),longestUniValuePath(root.right)))

def dfs(root):
    if not root:
        return 0
    res = 0
    if root.left and root.left.val == root.val:
        res = 1 + dfs(root.left)
    if root.right and root.right.val == root.val:
        res = max(res,1+dfs(root.right))
    return res

