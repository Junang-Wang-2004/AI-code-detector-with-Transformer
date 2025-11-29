class C1(object):

    def minSideJumps(self, a1):
        """
        """
        v1 = [1, 0, 1]
        for v2 in a1:
            if v2:
                v1[v2 - 1] = float('inf')
            for v3 in range(3):
                if v3 + 1 != v2:
                    v1[v3] = min(v1[0] + (v3 != 0), v1[1] + (v3 != 1), v1[2] + (v3 != 2))
        return min(v1)
