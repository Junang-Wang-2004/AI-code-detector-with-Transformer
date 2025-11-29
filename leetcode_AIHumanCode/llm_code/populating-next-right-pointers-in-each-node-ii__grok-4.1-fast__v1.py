class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return root
        level_start = root
        while level_start and level_start.left:
            walker = level_start
            while walker:
                walker.left.next = walker.right
                if walker.next:
                    walker.right.next = walker.next.left
                walker = walker.next
            level_start = level_start.left
        return root
