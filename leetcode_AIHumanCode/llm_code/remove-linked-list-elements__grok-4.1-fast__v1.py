class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if not head:
            return None

        prev_node = head
        next_node = head.next
        while next_node:
            if next_node.val == val:
                prev_node.next = next_node.next
            else:
                prev_node = next_node
            next_node = next_node.next

        return head
