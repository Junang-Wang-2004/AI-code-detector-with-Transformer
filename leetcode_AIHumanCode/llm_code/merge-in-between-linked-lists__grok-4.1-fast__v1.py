class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        dummy = ListNode(0)
        dummy.next = list1
        prev = dummy
        for _ in range(a):
            prev = prev.next
        nxt = prev.next
        for _ in range(b - a + 1):
            nxt = nxt.next
        prev.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = nxt
        return dummy.next
