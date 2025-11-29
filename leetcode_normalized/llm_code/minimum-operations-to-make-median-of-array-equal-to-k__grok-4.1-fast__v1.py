class C1:

    def minOperationsToMakeMedianK(self, a1, a2):
        v1 = len(a1)
        a1.sort()
        v2 = v1 // 2
        v3 = 0
        for v4 in range(v2 + 1):
            if a1[v4] > a2:
                v3 += a1[v4] - a2
        for v4 in range(v2, v1):
            if a1[v4] < a2:
                v3 += a2 - a1[v4]
        return v3
