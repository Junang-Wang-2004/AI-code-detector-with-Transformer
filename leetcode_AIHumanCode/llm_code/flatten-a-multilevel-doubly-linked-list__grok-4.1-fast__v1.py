class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        node = head
        while node:
            if node.child:
                subhead = node.child
                subtail = subhead
                while subtail.next:
                    subtail = subtail.next
                subtail.next = node.next
                if node.next:
                    node.next.prev = subtail
                node.next = subhead
                subhead.prev = node
                node.child = None
            node = node.next
        return head
