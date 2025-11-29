class C1(object):

    def maxJumps(self, a1, a2):
        """
        """
        v1, v2 = (list(range(len(a1))), [])
        for v3 in range(len(a1)):
            while v2 and a1[v2[-1]] < a1[v3]:
                if v3 - v2[-1] <= a2:
                    v1[v3] = v2[-1]
                v2.pop()
            v2.append(v3)
        v4, v2 = (list(range(len(a1))), [])
        for v3 in reversed(range(len(a1))):
            while v2 and a1[v2[-1]] < a1[v3]:
                if v2[-1] - v3 <= a2:
                    v4[v3] = v2[-1]
                v2.pop()
            v2.append(v3)
        v5 = SegmentTree(len(a1))
        for v6, v3 in sorted(([x, v3] for v3, v7 in enumerate(a1))):
            v5.update(v3, v3, v5.query(v1[v3], v4[v3]) + 1)
        return v5.query(0, len(a1) - 1)
