class C1(object):

    def lengthOfLIS(self, a1):
        """
        """
        v1 = {num: i for v2, v3 in enumerate(sorted(set(a1)))}
        v4 = SegmentTree(len(v1))
        for v5 in a1:
            v4.update(v1[v5], v1[v5], v4.query(0, v1[v5] - 1) + 1 if v1[v5] >= 1 else 1)
        return v4.query(0, len(v1) - 1) if len(v1) >= 1 else 0
