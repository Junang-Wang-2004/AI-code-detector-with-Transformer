class C1(object):

    def bestTeamScore(self, a1, a2):
        """
        """
        v1 = sorted(zip(a2, a1))
        v2 = sorted(set(a1))
        v3 = {score: i for v4, v5 in enumerate(v2)}
        v6 = SegmentTree(len(v3))
        v7 = 0
        for v8, v5 in v1:
            v6.update(v3[v5], v3[v5], v6.query(0, v3[v5]) + v5)
        return v6.query(0, len(v3) - 1)
