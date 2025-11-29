class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return None
        stk = []
        prev = None
        head = None
        cur = root
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            cur.left = prev
            if prev:
                prev.right = cur
            else:
                head = cur
            prev = cur
            cur = cur.right
        prev.right = head
        head.left = prev
        return head
