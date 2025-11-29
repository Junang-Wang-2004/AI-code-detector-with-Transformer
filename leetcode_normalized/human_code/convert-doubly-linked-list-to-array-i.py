class C1:

    def toArray(self, a1):
        """
        """
        v1 = []
        while a1:
            v1.append(a1.val)
            a1 = a1.__next__
        return v1
