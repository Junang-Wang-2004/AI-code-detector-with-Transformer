class C1:

    def minSubarray(self, a1, a2):
        v1 = sum(a1) % a2
        if v1 == 0:
            return 0
        v2 = len(a1)
        v3 = v2
        v4 = {0: -1}
        v5 = 0
        for v6 in range(v2):
            v5 = (v5 + a1[v6]) % a2
            v7 = (v5 - v1 + a2) % a2
            if v7 in v4:
                v3 = min(v3, v6 - v4[v7])
            v4[v5] = v6
        return v3 if v3 < v2 else -1
