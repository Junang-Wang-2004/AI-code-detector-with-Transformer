class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, num1, num2):
        prev = None
        head = None
        remainder = 0

        while num1 or num2 or remainder:
            d1 = num1.val if num1 else 0
            d2 = num2.val if num2 else 0
            total = d1 + d2 + remainder

            node = ListNode(total % 10)
            if head is None:
                head = node
            else:
                prev.next = node
            prev = node

            remainder = total // 10
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next

        return head
