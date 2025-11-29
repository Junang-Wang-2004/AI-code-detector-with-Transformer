class C1:

    def minimumSubstringsInPartition(self, a1):
        v1 = len(a1)
        v2 = float('inf')
        v3 = [v2] * (v1 + 1)
        v3[0] = 0
        for v4 in range(v1):
            v5 = [0] * 26
            v6 = 0
            v7 = 0
            for v8 in range(v4, v1):
                v9 = ord(a1[v8]) - ord('a')
                v5[v9] += 1
                if v5[v9] == 1:
                    v6 += 1
                v7 = max(v7, v5[v9])
                v10 = v8 - v4 + 1
                if v6 * v7 == v10:
                    v3[v8 + 1] = min(v3[v8 + 1], v3[v4] + 1)
        return v3[-1]
