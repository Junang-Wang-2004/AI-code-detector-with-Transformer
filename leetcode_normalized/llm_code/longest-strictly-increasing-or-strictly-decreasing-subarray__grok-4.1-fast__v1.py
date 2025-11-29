class C1:

    def longestMonotonicSubarray(self, a1):
        v1 = len(a1)
        if v1 <= 1:
            return v1
        v2 = 1
        v3 = 1
        v4 = 1
        for v5 in range(1, v1):
            if a1[v5 - 1] < a1[v5]:
                v3 += 1
                v4 = 1
            elif a1[v5 - 1] > a1[v5]:
                v4 += 1
                v3 = 1
            else:
                v3 = 1
                v4 = 1
            v2 = max(v2, v3, v4)
        return v2
