class C1:

    def maxChunksToSorted(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v2[0] = a1[0]
        for v3 in range(1, v1):
            v2[v3] = max(v2[v3 - 1], a1[v3])
        v4 = 0
        for v5 in range(v1):
            if v2[v5] == v5:
                v4 += 1
        return v4
