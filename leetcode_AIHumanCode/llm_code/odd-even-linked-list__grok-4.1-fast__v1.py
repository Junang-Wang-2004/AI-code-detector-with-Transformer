class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd_end = head
        even_start = head.next
        even_end = even_start
        while even_end and even_end.next:
            nxt_odd = even_end.next
            odd_end.next = nxt_odd
            odd_end = nxt_odd
            even_end.next = nxt_odd.next
            even_end = even_end.next
        odd_end.next = even_start
        return head
