class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def removeElements_1(head,val):
    while head != None and head.val == val:
        head = head.next
    node = head
    while node != None and node.next !=None :
        if node.next.val != val:
            node = node.next
        else:
            node.next = node.next.next
    return head

def removeElements_2(head,val):
    if not head :
        return head
    node = head
    while node.next != None:
        if node.next.val == val:
            node.next = node.next.next
        else:
            node = node.next
    return head.next if head.val == val else head

def removeElements(head,val):
    if not head:
        return head
    head.next = removeElements(head.next,val)
    return head if head.val != val else head.next




