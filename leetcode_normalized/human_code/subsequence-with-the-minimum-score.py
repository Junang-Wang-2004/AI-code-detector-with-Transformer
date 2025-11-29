class C1(object):

    def minimumScore(self, a1, a2):
        """
        """
        v1 = [-1] * len(a1)
        v2 = len(a2) - 1
        for v3 in reversed(range(len(a1))):
            if v2 >= 0 and a2[v2] == a1[v3]:
                v2 -= 1
            v1[v3] = v2
        v4 = v2 + 1
        v5 = 0
        for v3 in range(len(a1)):
            v4 = max(min(v4, v1[v3] - v5 + 1), 0)
            if v5 < len(a2) and a2[v5] == a1[v3]:
                v5 += 1
        v4 = min(v4, len(a2) - v5)
        return v4
