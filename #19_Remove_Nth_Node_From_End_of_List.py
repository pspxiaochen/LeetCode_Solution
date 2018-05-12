class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def removeNthFromEnd(head,n):
    temp = head
    l = 0
    while temp != None:
        temp = temp.next
        l += 1
    if l == n:
        return head.next
    temp = head
    while l >= n + 1:
        temp = temp.next
        l -= 1
    temp.next = temp.next.next
    return head

def removeNthFromEnd_2(head,n):
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
    if fast == None:
        return slow.next
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

