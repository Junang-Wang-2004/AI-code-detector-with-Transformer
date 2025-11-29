class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        sentinel = ListNode(0)
        sentinel.next = head
        ptr = sentinel
        for _ in range(m - 1):
            ptr = ptr.next
        seg_start = ptr.next
        seg_len = n - m + 1
        prev_seg = ptr
        curr_seg = ptr.next
        while seg_len > 0:
            next_seg = curr_seg.next
            curr_seg.next = prev_seg
            prev_seg = curr_seg
            curr_seg = next_seg
            seg_len -= 1
        ptr.next = prev_seg
        seg_start.next = curr_seg
        return sentinel.next
