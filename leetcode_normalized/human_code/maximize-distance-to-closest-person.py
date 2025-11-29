class C1(object):

    def maxDistToClosest(self, a1):
        """
        """
        v1, v2 = (-1, 1)
        for v3 in range(len(a1)):
            if a1[v3]:
                if v1 < 0:
                    v2 = v3
                else:
                    v2 = max(v2, (v3 - v1) // 2)
                v1 = v3
        return max(v2, len(a1) - 1 - v1)
