class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def depth(root):
    if not root:
        return 0
    return 1 + max(depth(root.left),depth(root.right))

def isBalanced_1(root):
    if not root:
        return True
    if not isBalanced_1(root.left):
        return False
    if not isBalanced_1(root.right):
        return False
    left_depth = depth(root.left)
    right_depth = depth(root.right)
    if -1>(left_depth - right_depth) or (left_depth - right_depth)>1:
        return False
    return True

################################
def isBalanced_2(root):
    return dfsHeight(root) != -1
def dfsHeight(root):
    if not root :
        return 0
    leftheight = dfsHeight(root.left)
    if leftheight == -1:
        return -1
    rightheight = dfsHeight(root.right)
    if rightheight == -1:
        return -1
    if (abs(leftheight - rightheight)>1):
        return -1
    return max(leftheight,rightheight)+1
