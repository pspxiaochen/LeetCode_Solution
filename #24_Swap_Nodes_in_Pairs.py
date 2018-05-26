class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def swapPairs(head):
    if not head or head.next ==None:
        return head
    res = ListNode(0)
    res.next = head
    f = res
    s = head
    while s != None and s.next != None:
        temp = s.next.next
        s.next.next = s
        f.next = s.next
        s.next = temp
        f = s
        s = temp
    return res.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
print(swapPairs(node1))
