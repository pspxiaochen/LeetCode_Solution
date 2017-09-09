class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth_1(root):
    return 1 + max(maxDepth_1(root.left),maxDepth_1(root.right)) if root else 0

#DFS
def maxDepth_2(root):
    if root is None:
        return 0
    nodeStack = []
    valueStack = []
    nodeStack.append(root)
    valueStack.append(1)
    maxDepth = 0
    while nodeStack:
        node = nodeStack.pop()
        temp = valueStack.pop()
        maxDepth = max(temp,maxDepth)
        if node.left:
            nodeStack.append(node.left)
            valueStack.append(temp+1)
        if node.right:
            nodeStack.append(node.right)
            valueStack.append(temp+1)
    return maxDepth
#BFS
import collections
def maxDepth_3(root):
    if root is None:
        return 0
    tqueue,h = collections.deque(),0
    tqueue.append(root)
    while tqueue:
        nextlevel = collections.deque()
        while tqueue:
            node = tqueue.popleft()
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        tqueue = nextlevel
        h += 1
    return h

