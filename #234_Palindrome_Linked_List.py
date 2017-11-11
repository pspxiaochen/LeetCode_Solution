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

