class C1(object):

    def minSideJumps(self, a1):
        """
        """
        v1, v2 = (0, set([2]))
        for v3 in range(len(a1) - 1):
            v2.discard(a1[v3 + 1])
            if v2:
                continue
            v1 += 1
            v2 = set((j for v4 in range(1, 4) if v4 not in [a1[v3], a1[v3 + 1]]))
        return v1
