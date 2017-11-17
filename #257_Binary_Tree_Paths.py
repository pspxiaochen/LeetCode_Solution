class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def binaryTreePath(root):
    paths = []
    if not root:
        return paths
    getPath(root,'',paths)
    return paths

def getPath(root,path,paths):
    if root.left == None and root.right == None:
        paths.append(path+str(root.val))
    if root.left != None:
        getPath(root.left,path + str(root.val) + '->',paths)
    if root.right != None:
        getPath(root.right,path + str(root.val) + '->' ,paths)

def binaryTreePath_2(root):
    if not root:
        return []
    paths,stack = [],[(root,"")]
    while len(stack) != 0:
        node,path = stack.pop()
        if not node.left and not node.right:
            paths.append(path + str(node.val))
        if node.left:
            stack.append((node.left,path + str(node.val) + '->'))
        if node.right:
            stack.append((node.right, path + str(node.val) + '->'))
    return paths