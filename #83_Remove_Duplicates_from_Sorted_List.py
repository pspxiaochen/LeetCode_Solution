class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


def deleteDuplicates_1(head):
    if head is None or head.next is None:
        return head
    p, q, r = ListNode(0), ListNode(0), ListNode(0)
    p = head
    while (p != None):
        q = p
        while (q.next != None):
            if (q.next.val == p.val):
                r = q.next
                q.next = r.next
                r = None
            else:
                q = q.next
        p = p.next
    return head

def deleteDuplicates_2(head):
    if head is None or head.next is None:
        return head
    head.next = deleteDuplicates_2(head.next)
    return head.next if head.val==head.next.val else head


def deleteDuplicates_3(head):
    list = ListNode(0)
    list = head
    while(list!=None):
        if(list.next==None):
            break
        elif(list.val == list.next.val):
            list.next = list.next.next
        else:
            list = list.next
    return list

