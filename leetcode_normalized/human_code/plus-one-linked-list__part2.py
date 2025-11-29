class C1(object):

    def plusOne(self, a1):
        """
        """

        def reverseList(a1):
            v1 = ListNode(0)
            v2 = a1
            while v2:
                v1.next, v2.next, v2 = (v2, v1.next, v2.next)
            return v1.__next__
        v1 = reverseList(a1)
        v2, v3 = (v1, 1)
        while v2 and v3:
            v2.val += v3
            v3 = v2.val / 10
            v2.val %= 10
            if v3 and v2.__next__ is None:
                v2.next = ListNode(0)
            v2 = v2.__next__
        return reverseList(v1)
