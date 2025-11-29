class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        newhead = head.next
        head.next = newhead.next
        newhead.next = head
        tail = head
        curr = tail.next
        while curr is not None and curr.next is not None:
            tail.next = curr.next
            curr.next = tail.next.next
            tail.next.next = curr
            tail = curr
            curr = tail.next
        return newhead
