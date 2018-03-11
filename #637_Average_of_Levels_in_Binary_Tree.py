class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
import collections
def averageOfLevels(root):
    ave = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        sum = 0.0
        count = 0.0
        temp = collections.deque()
        while queue:
            node = queue.pop()
            sum += node.val
            count += 1
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp
        ave.append(sum / count)
    return ave


