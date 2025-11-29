class Solution:
    def doubleIt(self, head):
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        rev_head = reverse(head)
        carry = 0
        tail = None
        curr = rev_head
        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10
            tail = curr
            curr = curr.next
        if carry:
            tail.next = ListNode(carry)
        return reverse(rev_head)
