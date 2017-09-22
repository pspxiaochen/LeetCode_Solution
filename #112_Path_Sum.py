class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def hasPathSum_1(root,sum):
    if not root:
        return False
    elif root.left is None and root.right is None and root.val == sum:
        return True
    else:
        return hasPathSum_1(root.left,sum - root.val) or hasPathSum_1(root.right,sum - root.val)
import collections
def hasPathSum_2(root,sum):
    if not root:
        return False
    nodes = collections.deque()
    values = collections.deque()

    nodes.append(root)
    values.append(root.val)
    while nodes:
        node = nodes.popleft()
        sumValue = values.popleft()
        if node.left == None and node.right == None and sumValue == sum:
            return True
        if node.left:
            nodes.append(node.left)
            values.append(sumValue + node.left.val)
        if node.right:
            nodes.append(node.right)
            values.append(sumValue + node.right.val)
    return False


