class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class Solution:
    def removeZeroSumSublists(self, head):
        sentinel = ListNode(0, head)
        sums_seen = {0: sentinel}
        walker = sentinel
        accum = 0
        while walker:
            accum += walker.val
            if accum in sums_seen:
                sums_seen[accum].next = walker.next
            else:
                sums_seen[accum] = walker
            walker = walker.next
        return sentinel.next
