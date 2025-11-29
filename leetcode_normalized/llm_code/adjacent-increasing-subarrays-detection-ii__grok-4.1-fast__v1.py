class C1:

    def maxIncreasingSubarrays(self, a1):
        v1 = 0
        v2 = 1
        v3 = 0
        v4 = len(a1)
        v5 = 1
        while v5 < v4:
            if a1[v5 - 1] < a1[v5]:
                v2 += 1
            else:
                v1 = max(v1, v2 // 2, min(v3, v2))
                v3 = v2
                v2 = 1
            v5 += 1
        v1 = max(v1, v2 // 2, min(v3, v2))
        return v1
