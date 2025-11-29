class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = [0] * (len(a2) + 1)
        for v2 in range(len(a1)):
            v3[v2 + 1] = v3[v2] + a2[v2]
        v4 = [float('inf')] * (len(a1) + 1)
        v4[-1] = 0
        for v2 in reversed(range(len(a1))):
            for v5 in range(v2, len(a1)):
                v4[v2] = min(v4[v2], v1[v5 + 1] * (v3[v5 + 1] - v3[v2]) + v4[v5 + 1] + a3 * (v3[-1] - v3[v2]))
        return v4[0]
