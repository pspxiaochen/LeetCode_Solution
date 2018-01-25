class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    diameter = 0
    def diameterOfBinaryTree(self,root):
        if not root:
            return self.diameter
        temp = self.countDeep(root.left) + self.countDeep(root.right)
        self.diameter = max(temp,self.diameter)
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.diameter

    def countDeep(self,root):
        return 1 + max(self.countDeep(root.left), self.countDeep(root.right)) if root else 0

class Solution_2(object):
    temp = 0
    def diameterOfBinaryTree(self,root):
        self.maxDepth(root)
        return self.temp

    def maxDepth(self,root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.temp = max(self.temp,left + right)
        return max(left,right) + 1
