class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitCircularLinkedList(self, lst):
        length = 1
        cur = lst.next
        while cur != lst:
            cur = cur.next
            length += 1
        half = length // 2
        split = lst
        for _ in range(half - 1):
            split = split.next
        head2 = split.next
        split.next = lst
        cur = head2
        while cur.next != lst:
            cur = cur.next
        cur.next = head2
        return [lst, head2]
