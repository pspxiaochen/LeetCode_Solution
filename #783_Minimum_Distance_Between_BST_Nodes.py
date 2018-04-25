class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def minDiffInBST(root):
    res = []
    res = helper(root,res)
    Min = 99999
    for i in range(1,len(res)):
        if res[i] - res[i-1] < Min:
            Min = res[i] - res[i-1]
    return Min


def helper(root,stack):
    if root.left:
        helper(root.left,stack)
    stack.append(root.val)
    if root.right:
        helper(root.right,stack)
    return stack

class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res

