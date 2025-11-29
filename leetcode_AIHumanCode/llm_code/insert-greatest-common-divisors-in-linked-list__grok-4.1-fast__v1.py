class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        def greatest_common_divisor(x, y):
            return x if y == 0 else greatest_common_divisor(y, x % y)

        ptr = head
        while ptr and ptr.next:
            g = greatest_common_divisor(ptr.val, ptr.next.val)
            temp = ptr.next
            ptr.next = ListNode(g, temp)
            ptr = temp
        return head
