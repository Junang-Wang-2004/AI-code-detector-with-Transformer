class C1:

    def longestSubarray(self, a1):
        v1 = len(a1)
        v2 = [i for v3 in range(v1 - 1) if a1[v3] > a1[v3 + 1]]
        v4 = [-1] + v2 + [v1 - 1]
        v5 = 0
        v6 = len(v4)
        for v3 in range(v6 - 1):
            v7 = v4[v3 + 1] - v4[v3]
            v5 = max(v5, v7)
        for v3 in range(v6 - 2):
            v8 = v4[v3 + 1] - v4[v3] + (v4[v3 + 2] - v4[v3 + 1])
            v5 = max(v5, v8)
        return v5
