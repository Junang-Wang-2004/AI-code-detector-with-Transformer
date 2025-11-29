class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def plusOne(self, head):
        if not head:
            return None

        last_non_nine = None
        tail = head
        while tail.next:
            if tail.val < 9:
                last_non_nine = tail
            tail = tail.next

        if tail.val < 9:
            tail.val += 1
            return head

        if last_non_nine is None:
            new_head = ListNode(1)
            temp = head
            while temp:
                temp.val = 0
                temp = temp.next
            new_head.next = head
            return new_head

        last_non_nine.val += 1
        temp = last_non_nine.next
        while temp:
            temp.val = 0
            temp = temp.next
        return head
