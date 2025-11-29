# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortLinkedList(self, head):
        neg_dummy = ListNode()
        pos_dummy = ListNode()
        neg_tail = neg_dummy
        pos_tail = pos_dummy
        node = head
        while node:
            if node.val > 0:
                pos_tail.next = node
                pos_tail = node
            else:
                neg_tail.next = node
                neg_tail = node
            node = node.next
        neg_tail.next = pos_dummy.next
        return neg_dummy.next
