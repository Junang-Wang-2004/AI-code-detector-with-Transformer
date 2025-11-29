class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        front, back = head, head.next
        while back and back.next:
            front = front.next
            back = back.next.next
        tail1 = front.next
        front.next = None
        left = self.sortList(head)
        right = self.sortList(tail1)
        return self._merge(left, right)

    def _merge(self, p: ListNode, q: ListNode) -> ListNode:
        sentinel = ListNode()
        walker = sentinel
        while p and q:
            if p.val <= q.val:
                walker.next = p
                p = p.next
            else:
                walker.next = q
                q = q.next
            walker = walker.next
        walker.next = p or q
        return sentinel.next
