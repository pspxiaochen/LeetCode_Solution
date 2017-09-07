class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def mergeTwoLists(l1,l2):
    node1 = node2 = ListNode(0)
    while l1 or l2:
        if l1 < l2:
            node1 = l1
            l1 = l1.next
        else:
            node1 = l2
            l2 = l2.next
        


