class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head):
        if not head:
            return 0
        return (self.getDecimalValue(head.next) << 1) | head.val
