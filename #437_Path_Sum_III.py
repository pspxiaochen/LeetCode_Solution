import collections
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root,sum):
    if not root:
        return 0
    queue = collections.deque()
    out = 0
    queue.append(root)
    while queue :
        for i in range(len(queue)):
            node = queue.popleft()
            out += canSum(node,sum,0)
            if node.left !=None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
    return out

def canSum(root,targetSum,tempSum):
    sumNumber = 0
    if not root :
        return sumNumber
    if root.val + tempSum == targetSum:
        sumNumber += 1
    sumNumber += canSum(root.left,targetSum,root.val+tempSum) + canSum(root.right,targetSum,root.val+tempSum)
    return sumNumber
######################################################################################################################

def pathSum_2(root,sum):
    if not root:
        return 0
    return pathSumFrom(root,sum) + pathSum_2(root.left,sum) + pathSum_2(root.right,sum)

def pathSumFrom(root,sum):
    if not root:
        return 0
    return (1 if root.val == sum else 0) + pathSumFrom(root.left,sum-root.val) + pathSumFrom(root.right,sum-root.val)


node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(-3)
node4 = TreeNode(3)
node5 = TreeNode(2)
node6 = TreeNode(11)
node7 = TreeNode(3)
node8 = TreeNode(-2)
node9 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7
node4.right = node8
node5.right = node9
print(pathSum(node1,8))