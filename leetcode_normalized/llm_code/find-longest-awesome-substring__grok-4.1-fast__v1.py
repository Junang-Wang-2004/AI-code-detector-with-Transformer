class C1:

    def longestAwesome(self, a1):
        v1 = len(a1)
        v2 = {0: -1}
        v3 = 0
        v4 = 0
        for v5 in range(v1):
            v6 = int(a1[v5])
            v4 ^= 1 << v6
            v3 = max(v3, v5 - v2.get(v4, v1))
            for v7 in range(10):
                v8 = v4 ^ 1 << v7
                v3 = max(v3, v5 - v2.get(v8, v1))
            if v4 not in v2:
                v2[v4] = v5
        return v3
