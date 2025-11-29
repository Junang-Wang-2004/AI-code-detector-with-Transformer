class C1(object):

    def maxPoints(self, a1):
        if not a1:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = a1[0][:]
        for v4 in range(1, v1):
            v5 = [0] * v2
            v5[0] = v3[0]
            for v6 in range(1, v2):
                v5[v6] = max(v5[v6 - 1] - 1, v3[v6])
            v7 = [0] * v2
            v7[v2 - 1] = v3[v2 - 1]
            for v6 in range(v2 - 2, -1, -1):
                v7[v6] = max(v7[v6 + 1] - 1, v3[v6])
            v8 = [0] * v2
            for v6 in range(v2):
                v8[v6] = a1[v4][v6] + max(v5[v6], v7[v6])
            v3 = v8
        return max(v3)
