class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        walker_slow = head
        walker_fast = head
        while walker_fast:
            if not walker_fast.next:
                return None
            walker_fast = walker_fast.next.next
            walker_slow = walker_slow.next
            if walker_slow == walker_fast:
                break
            if not walker_slow:
                return None
        else:
            return None
        walker_fast = head
        while walker_fast != walker_slow:
            walker_fast = walker_fast.next
            walker_slow = walker_slow.next
        return walker_fast
