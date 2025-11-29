class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, root):
        if not root or not root.next:
            return root

        front = root
        back = root.next
        while back and back.next:
            front = front.next
            back = back.next.next

        sec_start = front.next
        front.next = None

        prev = None
        cur = sec_start
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        first = root
        second = prev
        while first and second:
            f_next = first.next
            s_next = second.next
            first.next = second
            second.next = f_next
            first = f_next
            second = s_next

        return root
