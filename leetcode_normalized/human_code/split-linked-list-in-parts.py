class C1(object):

    def splitListToParts(self, a1, a2):
        """
        """
        v1 = 0
        v2 = a1
        while v2:
            v2 = v2.__next__
            v1 += 1
        v3, v4 = divmod(v1, a2)
        v5 = []
        v2 = a1
        for v6 in range(a2):
            v7 = v2
            for v8 in range(v3 - 1 + int(v6 < v4)):
                if v2:
                    v2 = v2.__next__
            if v2:
                v2.next, v2 = (None, v2.next)
            v5.append(v7)
        return v5
