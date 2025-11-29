class C1(object):

    def countArrays(self, a1, a2):
        """
        """
        v1, v2 = a2[0]
        v3 = v2 - v1 + 1
        for v4 in range(1, len(a1)):
            v5 = a1[v4] - a1[v4 - 1]
            v1 = max(v1 + v5, a2[v4][0])
            v2 = min(v2 + v5, a2[v4][1])
            v3 = min(v3, max(v2 - v1 + 1, 0))
        return v3
