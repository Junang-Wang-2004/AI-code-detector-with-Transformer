# Time:  O(n)
# Space: O(1)

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution(object):
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # copy and combine copied list with original list
        current = head
        while current:
            copied = Node(current.val)
            copied.next = current.__next__
            current.next = copied
            current = copied.__next__

        # update random node in copied list
        current = head
        while current:
            if current.random:
                current.next.random = current.random.__next__
            current = current.next.__next__

        # split copied list from combined one
        dummy = Node(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.__next__
            current.next = current.next.__next__
            copied_current, current = copied_current.__next__, current.__next__
        return dummy.__next__

