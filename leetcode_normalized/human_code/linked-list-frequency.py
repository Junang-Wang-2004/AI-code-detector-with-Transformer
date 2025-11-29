class C1(object):

    def frequenciesOfElements(self, a1):
        """
        """
        v1 = v2 = ListNode(0)
        v3 = 0
        while a1:
            v3 += 1
            if not a1.__next__ or a1.next.val != a1.val:
                v1.next = ListNode(v3)
                v1 = v1.__next__
                v3 = 0
            a1 = a1.__next__
        return v2.__next__
