class C1(object):

    def maximumOr(self, a1, a2):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in reversed(range(len(a1))):
            v1[v2] = v1[v2 + 1] | a1[v2]
        v3 = v4 = 0
        for v2 in range(len(a1)):
            v3 = max(v3, v4 | a1[v2] << a2 | v1[v2 + 1])
            v4 |= a1[v2]
        return v3
