class C1(object):

    def isArraySpecial(self, a1, a2):
        """
        """
        v1 = [0] * len(a1)
        for v2 in range(len(a1) - 1):
            v1[v2 + 1] = v1[v2] + int(a1[v2 + 1] & 1 != a1[v2] & 1)
        v3 = [False] * len(a2)
        for v2, (v4, v5) in enumerate(a2):
            v3[v2] = v1[v5] - v1[v4] == v5 - v4
        return v3
