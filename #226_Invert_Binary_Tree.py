class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
import collections
def invertTree_1(root):
    if not root:
        return root
    myQueue=collections.deque()
    myQueue.append(root)
    while(len(myQueue)!=0):
        node = myQueue.popleft()
        if node.left != None:
            myQueue.append(node.left)
            print(node.left.val)
        if node.right != None:
            myQueue.append(node.right)
            print(node.right.val)
        temp = node.left
        node.left = node.right
        node.right = temp
    return root

def invertTree_2(root):
    if not root:
        return None
    print(root.val)
    left = root.left
    right = root.right
    root.left = invertTree_2(right)
    root.right = invertTree_2(left)
    return root

def invertTree_3(root):
    if not root:
        return None
    stack = []
    stack.append(root)
    while(len(stack)!=0):
        node = stack.pop()
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
        temp = node.left
        node.left = node.right
        node.right = temp
    return root
