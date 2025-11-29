class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        sentinel = ListNode(-1)
        sentinel.next = head
        walker = sentinel
        while walker.next:
            if walker.next.next and walker.next.val == walker.next.next.val:
                dup_val = walker.next.val
                while walker.next and walker.next.val == dup_val:
                    walker.next = walker.next.next
            else:
                walker = walker.next
        return sentinel.next
