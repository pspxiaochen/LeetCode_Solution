class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def isPalindrome_1(head):
    if not head:
        return True
    list = []
    list.append(head.val)
    while head.next!=None:
        head = head.next
        list.append(head.val)
    return list == list[::-1]

def isPalindrome_2(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        temp = rev
        rev = slow
        slow = slow.next
        rev.next = temp
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        rev = rev.next
        slow = slow.next
    return not rev
