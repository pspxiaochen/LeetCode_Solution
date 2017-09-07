class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None



def isSameTree_1(p,q):
    if p and q:
        return p.val == q.val and isSameTree_1(p.left,q.left) and isSameTree_1(p.right,q.right)
    return p == q

def isSameTree_2(p,q):
    if(p == None and q ==None):
        return True
    if(p == None or q == None):
        return False
    if(p.val == q.val):
        return isSameTree_2(p.left,q.left) and isSameTree_2(p.right,q.right)
    return False

