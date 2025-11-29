class C1(object):

    def insertGreatestCommonDivisors(self, a1):

        def greatest_common_divisor(a1, a2):
            return a1 if a2 == 0 else greatest_common_divisor(a2, a1 % a2)
        v1 = a1
        while v1 and v1.next:
            v2 = greatest_common_divisor(v1.val, v1.next.val)
            v3 = v1.next
            v1.next = ListNode(v2, v3)
            v1 = v3
        return a1
