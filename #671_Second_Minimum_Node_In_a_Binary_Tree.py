class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
# 用了辅助函数的DFS
def findSecondMinimumValue(root):
    tmp = root.val
    a = set()
    a = help(a, root, tmp)
    return min(a) if len(a) != 0 else -1

def help(set,root,tmp):
    if root.val != tmp:
        set.add(root.val)
    if root.left:
         help(set,root.left,tmp)
    if root.right:
         help(set,root.right,tmp)
    return set

# 不用辅助函数的DFS

def findSecondMinimumValue_2(root):
    if not root:
        return -1
    if not root.left and  not root.right:
        return -1
    left = root.left.val
    right = root.right.val

    if root.left.val == root.val:
        left = findSecondMinimumValue_2(root.left)
    if root.right.val == root.val:
        right = findSecondMinimumValue_2(root.right)

    if left != -1 and right != -1:
        return min(left,right)
    elif left != -1 :
        return left
    else:
        return right

#BFS
def findSecondMinimumValue_3(root):
    rootVal = root.val
    small = 9999
    nodeList = []
    nodeList.append(root)
    diffFound = False
    while (len(nodeList)!=0):
        node = nodeList.pop()
        if node.val != rootVal and node.val < small:
            small = node.val
            diffFound = True
        if node.left:
            nodeList.append(node.left)
            nodeList.append(node.right)
    return -1 if not diffFound else small

