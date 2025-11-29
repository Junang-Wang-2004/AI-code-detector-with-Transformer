# Time:  O(n)
# Space: O(n)
# Recursive solution.
class Solution2(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin

    def reverseListRecu(self, head):
        if not head:
            return [None, None]

        [begin, end] = self.reverseListRecu(head.__next__)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]

