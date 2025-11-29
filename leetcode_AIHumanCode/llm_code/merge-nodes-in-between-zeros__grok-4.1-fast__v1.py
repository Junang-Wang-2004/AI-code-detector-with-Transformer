class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head):
        ptr = head
        while ptr.next:
            acc = 0
            scout = ptr.next
            while scout.val != 0:
                acc += scout.val
                scout = scout.next
            ptr.val += acc
            if not scout.next:
                ptr.next = None
                break
            ptr.next = scout
            ptr = scout
        return head
