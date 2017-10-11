class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def getIntersectionNode_1(headA,headB):
    if not headA or not headB:
        return None
    temp1 = headA
    temp2 = headB
    i = 0
    j = 0
    while temp1:
        temp1 = temp1.next
        i += 1
    while temp2:
        temp2 = temp2.next
        j += 1
    temp1 = headA
    temp2 = headB
    if i>j:
        for x in range(i-j):
            temp1 = temp1.next
    if j>i:
        for y in range(j-i):
            temp2 = temp2.next
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1
        else:
            temp1 = temp1.next
            temp2 = temp2.next
    return None

def getIntersectionNode_2(headA,headB):
    if not headA or not headB:
        return None
    temp1 = headA
    temp2 = headB
    while temp1 != temp2:
        temp1 = headB if temp1 == None else temp1.next
        temp2 = headA if temp2 == None else temp2.next
    return temp1



