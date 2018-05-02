class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    return helper(l1, l2, 0)

def helper(l1, l2, carry):
    if not l1 and not l2 and carry == 0:
        return None
    sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + carry
    carry = 1 if sum > 9 else 0
    value = sum % 10
    res = ListNode(value)
    res.next = helper(None if l1 == None else l1.next, None if l2 == None else l2.next, carry)
    return res

def addTwoNumbers_2(l1,l2):
    curr = dummy = ListNode(0)
    left = 0
    while l1 or l2 or left == 1:
        num1 = l1.val if l1 else 0
        l1 = l1.next if l1 else None
        num2 = l2.val if l2 else 0
        l2 = l2.next if l2 else None
        num = (num1 + num2 + left) % 10
        left = (num1 + num2 + left) // 10
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


