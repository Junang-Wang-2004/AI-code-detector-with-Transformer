class C1:

    def maximumAlternatingSubarraySum(self, a1):
        v1 = float('-inf')
        v2 = float('-inf')
        v3 = float('-inf')
        for v4 in a1:
            v5 = v4
            if v3 != float('-inf'):
                v5 = max(v5, v3 + v4)
            v6 = float('-inf')
            if v2 != float('-inf'):
                v6 = v2 - v4
            v1 = max(v1, v5, v6)
            v2 = v5
            v3 = v6
        return v1
