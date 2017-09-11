class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node1.left = node2
# node1.right = node3
import collections
def levelOrderBottom_1(root):
    out = []
    node = collections.deque()
    if root is None:
        return out
    out.append([root.val])
    node.append(root)
    while node:
        nodenext = collections.deque()
        out2 = []
        while node:
            top = node.popleft()
            if top.left:
                nodenext.append(top.left)
                out2.append(top.left.val)
            if top.right:
                nodenext.append(top.right)
                out2.append(top.right.val)
        node = nodenext
        if out2:
            out.append(out2)
    return out[::-1]
#########################################
def levelOrderBottom_2(root):
    res = []
    dfs(root,0,res)
    return res

def dfs(root,level,res):
    if root:
        if len(res) < level + 1:
            res.insert(0,[])
        res[-(level+1)].append(root.val)
        dfs(root.left,level+1,res)
        dfs(root.right,level+1,res)
##############################

def levelOrderBottom_3(root):
    res = []
    stack=[(root,0)]
    while stack:
        node, level = stack.pop()
        if node:
            if len(res) < level + 1:
                res.insert(0,[])
            res[-(level+1)].append(node.val)
            stack.append((node.right,level+1))
            stack.append((node.left,level+1))
    return res

def levelOrderBottom_4(root):
    res = []
    queue,level = collections.deque(),0
    queue.append((root,level))
    while queue:
        node,level= queue.popleft()
        if node:
            if len(res) < level + 1:
                res.insert(0,[])
            res[-(level+1)].append(node.val)
            queue.append((node.left,level + 1))
            queue.append((node.right,level + 1))
    return res

