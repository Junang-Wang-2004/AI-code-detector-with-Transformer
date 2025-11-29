class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)
        curr_small = small
        curr_large = large
        current = head
        while current:
            if current.val < x:
                curr_small.next = current
                curr_small = curr_small.next
            else:
                curr_large.next = current
                curr_large = curr_large.next
            current = current.next
        curr_small.next = large.next
        curr_large.next = None
        return small.next
