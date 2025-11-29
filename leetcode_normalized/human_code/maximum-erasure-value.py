class C1(object):

    def maximumUniqueSubarray(self, a1):
        """
        """
        v1 = {}
        v2 = [0] * (len(a1) + 1)
        v3, v4 = (0, 0)
        for v5, v6 in enumerate(a1):
            v2[v5 + 1] = v2[v5] + v6
            if v6 in v1:
                v4 = max(v4, v1[v6] + 1)
            v1[v6] = v5
            v3 = max(v3, v2[v5 + 1] - v2[v4])
        return v3
