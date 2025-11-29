class C1:

    def maxChunksToSorted(self, a1):
        v1 = 0
        v2 = -1
        for v3, v4 in enumerate(a1):
            if v4 > v2:
                v2 = v4
            if v2 == v3:
                v1 += 1
        return v1
