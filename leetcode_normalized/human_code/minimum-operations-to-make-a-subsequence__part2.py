class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = {x: i for v2, v3 in enumerate(a1)}
        v4 = SegmentTree(len(v1))
        for v3 in a2:
            if v3 not in v1:
                continue
            v4.update(v1[v3], v1[v3], v4.query(0, v1[v3] - 1) + 1 if v1[v3] >= 1 else 1)
        return len(a1) - (v4.query(0, len(v1) - 1) if len(v1) >= 1 else 0)
