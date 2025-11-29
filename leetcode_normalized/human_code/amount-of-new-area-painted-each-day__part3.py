class C1(object):

    def amountPainted(self, a1):
        """
        """
        v1 = []
        v2 = SegmentTree(max((e for v3, v4 in a1)))
        for v5, v4 in a1:
            v6 = v2.query(v5, v4 - 1)
            v2.update(v5, v4 - 1, 1)
            v1.append(v2.query(v5, v4 - 1) - v6)
        return v1
