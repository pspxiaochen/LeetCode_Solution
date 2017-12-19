class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def sumOfLeftLeaves_1(root):
    sum = 0
    if not root:
        return sum
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.left != None:
            stack.append(node.left)
            if not node.left.left and not node.left.right:
                sum += node.left.val
        if node.right != None:
            stack.append(node.right)
    return sum

def sumOfLeftLeaves_2(root):
    if not root:
        return 0
    sum = 0
    if root.left != None:
        if not root.left.left and not root.left.right:
            sum += root.left.val
        else:
            sum += sumOfLeftLeaves_2(root.left)
    sum += sumOfLeftLeaves_2(root.right)
    return sum


