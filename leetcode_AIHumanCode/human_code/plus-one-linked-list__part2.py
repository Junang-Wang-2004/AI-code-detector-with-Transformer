# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def plusOne(self, head):
        """
        """
        def reverseList(head):
            dummy = ListNode(0)
            curr = head
            while curr:
                dummy.next, curr.next, curr = curr, dummy.next, curr.next
            return dummy.__next__

        rev_head = reverseList(head)
        curr, carry = rev_head, 1
        while curr and carry:
            curr.val += carry
            carry = curr.val / 10
            curr.val %= 10
            if carry and curr.__next__ is None:
                curr.next = ListNode(0)
            curr = curr.__next__

        return reverseList(rev_head)

