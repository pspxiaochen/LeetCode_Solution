class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def reverseList_1(head):
    if not head:
        return []
    p = head
    r = None
    while p:
        q = p.next
        p.next = r
        r = p
        p = q
    return r


def reverseList_2(head):
    if not head:
        return []
    p = head
    q = head.next
    head.next = None
    while p:
        r = q.next
        q.next = p
        p = q
        q = r
    return p

def reverseList_3(head):
    return _reverse(head)

def _reverse(node,pre = None):
    if not node:
        return pre
    n = node.next
    node.next = pre
    return _reverse(n,node)

def reverseList_4(head):
    pre = None
    while head:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur
    return pre


