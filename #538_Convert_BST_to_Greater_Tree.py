class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    count = 0
    def convertBST(self,root):
        if not root:
            return root
        self.convertBST(root.right)
        self.count = root.val + self.count
        root.val = self.count
        self.convertBST(root.left)
        return root

def convertBST_2(root):
    if not root :
        return root
    total = 0
    stack = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.right
        node = stack.pop()
        total += node.val
        node.val = total
        node = node.left
    return root