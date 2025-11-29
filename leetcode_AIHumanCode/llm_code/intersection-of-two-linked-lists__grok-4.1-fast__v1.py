class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def length(head):
            count = 0
            node = head
            while node:
                count += 1
                node = node.next
            return count
        
        len_a = length(headA)
        len_b = length(headB)
        
        ptr_a = headA
        ptr_b = headB
        
        if len_a > len_b:
            for _ in range(len_a - len_b):
                ptr_a = ptr_a.next
        elif len_b > len_a:
            for _ in range(len_b - len_a):
                ptr_b = ptr_b.next
        
        while ptr_a != ptr_b:
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
        
        return ptr_a
