class C1(object):

    def maxHammingDistances(self, a1, a2):
        """
        """
        v1 = [float('-inf')] * (1 << a2)
        for v2 in a1:
            v1[v2] = 0
        for v3 in range(a2):
            v4 = v1[:]
            for v5 in range(1 << a2):
                v4[v5] = max(v4[v5], v1[v5 ^ 1 << v3] + 1)
            v1 = v4
        return [v1[v2] for v2 in a1]
