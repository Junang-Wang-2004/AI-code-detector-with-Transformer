class C1(object):

    def maxValue(self, a1):
        """
        """
        v1 = [float('inf')] * (len(a1) + 1)
        for v2 in reversed(range(len(a1))):
            v1[v2] = min(v1[v2 + 1], a1[v2])
        v3 = [0] * len(a1)
        v4 = v5 = 0
        for v6 in range(len(a1)):
            v4 = max(v4, a1[v6])
            if v4 > v1[v6 + 1]:
                continue
            while v5 <= v6:
                v3[v5] = v4
                v5 += 1
        return v3
