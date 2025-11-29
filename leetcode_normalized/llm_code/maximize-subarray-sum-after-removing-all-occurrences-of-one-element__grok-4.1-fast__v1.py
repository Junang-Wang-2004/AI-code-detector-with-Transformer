class C1:

    def maxSubarraySum(self, a1):
        if not a1:
            return 0
        v1 = float('-inf')
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = {}
        for v6 in a1:
            v2 += v6
            v1 = max(v1, v2 - v3)
            if v6 < 0:
                v7 = v5.get(v6, float('inf'))
                v8 = min(v7, v4) + v6
                v5[v6] = v8
                v3 = min(v3, v8)
            v4 = min(v4, v2)
            v3 = min(v3, v4)
        return v1
