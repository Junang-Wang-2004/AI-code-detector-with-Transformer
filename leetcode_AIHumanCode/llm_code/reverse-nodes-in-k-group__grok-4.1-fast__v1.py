class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_end = dummy
        while True:
            temp = prev_end
            for _ in range(k):
                temp = temp.next
                if temp is None:
                    return dummy.next
            group_start = prev_end.next
            new_head = self._reverse_group(group_start, k)
            prev_end.next = new_head
            prev_end = group_start

    def _reverse_group(self, head, k):
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head.next = curr
        return prev
