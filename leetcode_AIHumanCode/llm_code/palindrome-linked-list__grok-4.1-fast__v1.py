class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
