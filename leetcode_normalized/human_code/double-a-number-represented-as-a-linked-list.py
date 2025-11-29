class C1(object):

    def doubleIt(self, a1):
        """
        """
        if a1.val >= 5:
            a1 = ListNode(0, a1)
        v2 = a1
        while v2:
            v2.val = v2.val * 2 % 10
            if v2.__next__ and v2.next.val >= 5:
                v2.val += 1
            v2 = v2.__next__
        return a1
