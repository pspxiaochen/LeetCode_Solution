class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def findTilt(self,root):
        if root is None:
            return 0
        return  abs(self.countSum(root.left) - self.countSum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
    def countSum(self,root):
        if root is None:
            return 0
        else :
            return root.val + self.countSum(root.left) + self.countSum(root.right)
