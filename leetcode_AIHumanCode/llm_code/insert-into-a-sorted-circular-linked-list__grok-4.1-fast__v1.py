class Node(object):
    def __init__(self, x, y=None):
        self.val = x
        self.next = y


class Solution(object):
    def insert(self, head, insertVal):
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node
        new = Node(insertVal, None)
        begin = head
        p = head
        q = head.next
        while q != begin:
            if p.val > q.val:
                if insertVal >= p.val or insertVal <= q.val:
                    break
            if p.val <= insertVal < q.val:
                break
            p = q
            q = q.next
        p.next = new
        new.next = q
        return head
