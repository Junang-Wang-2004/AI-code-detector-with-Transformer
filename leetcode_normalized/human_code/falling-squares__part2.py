class C1(object):

    def fallingSquares(self, a1):
        v1 = set()
        for v2, v3 in a1:
            v1.add(v2)
            v1.add(v2 + v3 - 1)
        v1 = sorted(list(v1))
        v4 = SegmentTree(len(v1), max, max, 0)
        v5 = 0
        v6 = []
        for v2, v3 in a1:
            v7, v8 = (bisect.bisect_left(v1, v2), bisect.bisect_left(v1, v2 + v3 - 1))
            v9 = v4.query(v7, v8) + v3
            v4.update(v7, v8, v9)
            v5 = max(v5, v9)
            v6.append(v5)
        return v6
