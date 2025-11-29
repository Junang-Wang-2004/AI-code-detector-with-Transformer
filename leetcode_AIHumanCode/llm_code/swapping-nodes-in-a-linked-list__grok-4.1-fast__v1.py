class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        ptr1 = head
        for _ in range(k - 1):
            ptr1 = ptr1.next
        ptr2 = head
        ptr = ptr1
        while ptr.next:
            ptr = ptr.next
            ptr2 = ptr2.next
        ptr1.val, ptr2.val = ptr2.val, ptr1.val
        return head
