class C1:

    def maxBoxesInWarehouse(self, a1, a2):
        a1.sort()
        v1 = float('inf')
        v2 = []
        for v3 in a2:
            v1 = min(v1, v3)
            v2.append(v1)
        v4 = 0
        v5 = 0
        for v6 in range(len(v2) - 1, -1, -1):
            if v4 < len(a1) and a1[v4] <= v2[v6]:
                v5 += 1
                v4 += 1
        return v5
