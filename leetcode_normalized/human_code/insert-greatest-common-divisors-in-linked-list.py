class C1(object):

    def insertGreatestCommonDivisors(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = a1
        while v1.__next__:
            v1.next = ListNode(gcd(v1.val, v1.next.val), v1.next)
            v1 = v1.next.__next__
        return a1
