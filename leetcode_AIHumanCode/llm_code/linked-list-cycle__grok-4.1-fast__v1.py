class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
