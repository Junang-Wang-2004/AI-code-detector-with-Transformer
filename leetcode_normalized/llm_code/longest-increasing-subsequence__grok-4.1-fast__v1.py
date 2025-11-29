class C1:

    def lengthOfLIS(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = [1] * v1
        v3 = 1
        for v4 in range(v1):
            for v5 in range(v4):
                if a1[v5] < a1[v4]:
                    v2[v4] = max(v2[v4], v2[v5] + 1)
            v3 = max(v3, v2[v4])
        return v3
