class C1:

    def minHeightShelves(self, a1, a2):
        v1 = len(a1)
        v2 = float('inf')
        v3 = [v2] * (v1 + 1)
        v3[0] = 0
        for v4 in range(1, v1 + 1):
            v5 = 0
            v6 = 0
            v7 = v4 - 1
            while v7 >= 0:
                v5 += a1[v7][0]
                v6 = max(v6, a1[v7][1])
                if v5 > a2:
                    break
                v3[v4] = min(v3[v4], v3[v7] + v6)
                v7 -= 1
        return v3[v1]
