class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        ptr1 = ptr2 = head
        while ptr2.next and ptr2.next.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        prev_node = None
        cur_node = ptr1.next
        while cur_node:
            temp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp
        max_val = 0
        front = head
        back = prev_node
        while front and back:
            max_val = max(max_val, front.val + back.val)
            front = front.next
            back = back.next
        return max_val
