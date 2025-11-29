class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        if not head:
            return None
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        target = length // 2
        if target == 0:
            return head.next
        before = head
        for _ in range(target - 1):
            before = before.next
        before.next = before.next.next
        return head
