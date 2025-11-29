# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Two pointers solution.
class Solution(object):
    def plusOne(self, head):
        """
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, head
        while right.__next__:
            if right.val != 9:
                left = right
            right = right.__next__

        if right.val != 9:
            right.val += 1
        else:
            left.val += 1
            right = left.__next__
            while right:
                right.val = 0
                right = right.__next__

        return dummy if dummy.val else dummy.__next__


