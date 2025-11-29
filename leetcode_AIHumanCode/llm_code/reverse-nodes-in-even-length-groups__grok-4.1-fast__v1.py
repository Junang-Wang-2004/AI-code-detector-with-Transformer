class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head):
        ptr = head
        sz = 2
        while ptr and ptr.next:
            scanner = ptr
            count = 0
            for _ in range(sz):
                if not scanner.next:
                    break
                count += 1
                scanner = scanner.next
            sz += 1
            if count % 2 != 0:
                ptr = scanner
                continue
            group_first = ptr.next
            reversed_head = None
            walker = group_first
            for _ in range(count):
                following = walker.next
                walker.next = reversed_head
                reversed_head = walker
                walker = following
            group_first.next = walker
            ptr.next = reversed_head
            ptr = group_first
        return head
