class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists_1(l1, l2):
    Node1 = Node2 = ListNode(0)
    while(l1 and l2):
        if(l1.val<l2.val):
            Node1.next = l1
            l1 = l1.next
        else:
            Node1.next = l2
            l2 = l2.next
        Node1 = Node1.next
    Node1.next = l1 or l2
    return Node2.next

def mergeTwoLists_2(l1,l2):
    if not l1 or l2:
        return l1 or l2
    if l1.val<l2.val:
        l1.next = mergeTwoLists_2(l1.next,l2)
        return l1
    else:
        l2.next = mergeTwoLists_2(l1,l2.next)
        return l2

def mergeTwoLists_3(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    node1 = node2 = ListNode(0)
    node1.next = l1
    while(l1 and l2 ):
        if(l1.val < l2.val):
            l1 = l1.next
        else:
            nxt = node2.next
            node2.next = l2
            temp = l2.next
            l2.next = nxt
            l2 = temp
        node2 = node2.next
    node2.next = l1 or l2
    return node1.next




l1 = ListNode(-2)
l2 = ListNode(0)

print(mergeTwoLists_3(l1,l2).next.val)
