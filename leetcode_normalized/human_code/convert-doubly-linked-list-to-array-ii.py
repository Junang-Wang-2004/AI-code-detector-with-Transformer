class C1:

    def toArray(self, a1):
        """
        """
        while a1.prev:
            a1 = a1.prev
        v2 = []
        while a1:
            v2.append(a1.val)
            a1 = a1.__next__
        return v2
