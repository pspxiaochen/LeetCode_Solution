class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def minDepth_1(root):
    if not root:
        return 0
    if not root.left:
        return minDepth_1(root.right) + 1
    if not root.right:
        return minDepth_1(root.left) + 1
    return min(minDepth_1(root.left),minDepth_1(root.right)) + 1
import collections
def minDepth_2(root):
    if not root:
        return 0
    queue = collections.deque()
    queue.append(root)
    i = 0
    while queue:
        i += 1
        k = len(queue)
        for j in range(k):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append((node.right))
            if not node.right and not node.left:
                return i
    return -1



