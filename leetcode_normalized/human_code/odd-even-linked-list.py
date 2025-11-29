class C1(object):

    def oddEvenList(self, a1):
        """
        """
        if a1:
            v1, v2 = (a1, a1.__next__)
            while v2 and v2.__next__:
                v3 = v1.__next__
                v1.next = v2.__next__
                v1 = v1.__next__
                v2.next = v1.__next__
                v1.next = v3
                v2 = v2.__next__
        return a1
