class Solution:
    def frequenciesOfElements(self, head):
        dummy = ListNode(0)
        tail = dummy
        while head:
            length = 1
            next_node = head.next
            while next_node and next_node.val == head.val:
                length += 1
                next_node = next_node.next
            tail.next = ListNode(length)
            tail = tail.next
            head = next_node
        return dummy.next
