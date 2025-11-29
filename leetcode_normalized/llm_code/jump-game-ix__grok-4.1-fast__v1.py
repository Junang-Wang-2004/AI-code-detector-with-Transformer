class C1:

    def maxValue(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return []
        v2 = [0] * v1
        v2[0] = a1[0]
        for v3 in range(1, v1):
            v2[v3] = max(v2[v3 - 1], a1[v3])
        v4 = [0.0] * (v1 + 1)
        v4[v1] = float('inf')
        for v3 in range(v1 - 1, -1, -1):
            v4[v3] = min(v4[v3 + 1], a1[v3])
        v5 = [0] * v1
        for v3 in range(v1 - 1, -1, -1):
            if v2[v3] <= v4[v3 + 1]:
                v5[v3] = v2[v3]
            else:
                v5[v3] = v5[v3 + 1]
        return v5
