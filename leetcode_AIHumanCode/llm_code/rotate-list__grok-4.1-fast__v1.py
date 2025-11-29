class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head or head.next is None:
            return head
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        tail = curr
        k %= length
        if k == 0:
            return head
        prev = head
        for _ in range(length - k - 1):
            prev = prev.next
        newhead = prev.next
        prev.next = None
        tail.next = head
        return newhead
