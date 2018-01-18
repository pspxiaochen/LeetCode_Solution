class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

from collections import Counter
def findMode(root):
    if root is None:
        return []
    seed = []
    seed = addNode(seed,root)
    seed = (Counter(seed)).most_common()
    out = [seed[0][0]]
    for i in range(1,len(seed)):
        if seed[i][1] == seed[0][1]:
            out.append(seed[i][0])
        else:
            break
    return out

def addNode(list,root):
    if root.left is not None:
        addNode(list,root.left)
    list.append(root.val)
    if root.right is not None:
        addNode(list,root.right)
    return list

################################################
class Solution(object):
    def dfs_findMode(self,root):
        if not root:
            return
        self.dfs_findMode(root.left)
        self.tempcount += 1
        if root.val != self.curval:
            self.curval = root.val
            self.tempcount = 1
        if self.tempcount > self.maxcount:
            self.maxcount = self.tempcount
            self.res = []
            self.res.append(root.val)
        elif self.tempcount == self.maxcount:
            self.res.append(root.val)
        self.dfs_findMode(root.right)

    def findMode(self,root):
        self.curval = 0
        self.tempcount = 0
        self.maxcount = 0
        self.res = []
        if not root:
            return []
        self.dfs_findMode(root)
        return self.res
