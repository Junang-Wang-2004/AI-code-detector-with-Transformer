class C1(object):

    def maxSumTwoNoOverlap(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [float('-inf')] * (v1 + 1)
        v5 = [float('-inf')] * (v1 + 1)
        for v3 in range(1, v1 + 1):
            v4[v3] = v4[v3 - 1]
            v5[v3] = v5[v3 - 1]
            if v3 >= a2:
                v4[v3] = max(v4[v3], v2[v3] - v2[v3 - a2])
            if v3 >= a3:
                v5[v3] = max(v5[v3], v2[v3] - v2[v3 - a3])
        v6 = float('-inf')
        for v7 in range(a3, v1 + 1):
            v6 = max(v6, v4[v7 - a3] + v2[v7] - v2[v7 - a3])
        for v7 in range(a2, v1 + 1):
            v6 = max(v6, v5[v7 - a2] + v2[v7] - v2[v7 - a2])
        return v6
