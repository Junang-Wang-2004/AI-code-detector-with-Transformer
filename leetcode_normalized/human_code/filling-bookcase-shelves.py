class C1(object):

    def minHeightShelves(self, a1, a2):
        """
        """
        v1 = [float('inf') for v2 in range(len(a1) + 1)]
        v1[0] = 0
        for v3 in range(1, len(a1) + 1):
            v4 = a2
            v5 = 0
            for v6 in reversed(range(v3)):
                if v4 - a1[v6][0] < 0:
                    break
                v4 -= a1[v6][0]
                v5 = max(v5, a1[v6][1])
                v1[v3] = min(v1[v3], v1[v6] + v5)
        return v1[len(a1)]
