class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST_1(nums):
    if len(nums) == 0:
        return None
    head = helper(nums,0,len(nums)-1)
    return head

def helper(nums,low,high):
    if low > high:
        return None
    mid = int((low + high) / 2)
    node = TreeNode(nums[mid])
    node.left = helper(nums,low,mid - 1)
    node.right = helper(nums,mid+1,high)
    return node

def sortedArrayToBST_2(nums):
    if not nums:
        return None
    mid = len(nums)// 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST_2(nums[:mid-1])
    root.right = sortedArrayToBST_2(nums[mid+1:])
    return root

