# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dummy = Node(0)
        current, prev, copies = head, dummy, {}

        while current:
            copied = Node(current.val)
            copies[current] = copied
            prev.next = copied
            prev, current = prev.__next__, current.__next__

        current = head
        while current:
            if current.random:
                copies[current].random = copies[current.random]
            current = current.__next__

        return dummy.__next__

# time: O(n)
# space: O(n)
from collections import defaultdict


class Solution3(object):
    def copyRandomList(self, head):
        """
        """
        clone = defaultdict(lambda: Node(0))
        clone[None] = None
        cur = head

        while cur:
            clone[cur].val = cur.val
            clone[cur].next = clone[cur.__next__]
            clone[cur].random = clone[cur.random]
            cur = cur.__next__

        return clone[head]
