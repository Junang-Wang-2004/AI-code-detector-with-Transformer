class C1(object):

    def maximumSubarraySum(self, a1, a2):
        v1 = {}
        v2 = 0
        v3 = float('-inf')
        for v4 in a1:
            if v4 not in v1:
                v1[v4] = v2
            else:
                v1[v4] = min(v1[v4], v2)
            for v5 in [-a2, a2]:
                v6 = v4 + v5
                if v6 in v1:
                    v7 = v2 + v4
                    v8 = v7 - v1[v6]
                    v3 = max(v3, v8)
            v2 += v4
        return v3 if v3 != float('-inf') else 0
