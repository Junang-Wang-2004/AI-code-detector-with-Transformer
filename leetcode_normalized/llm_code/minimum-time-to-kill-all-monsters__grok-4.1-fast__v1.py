class C1:

    def minimumTime(self, a1):
        v1 = len(a1)
        v2 = 1 << v1
        v3 = float('inf')
        v4 = [v3] * v2
        v4[0] = 0
        for v5 in range(v2):
            v6 = bin(v5).count('1')
            for v7 in range(v1):
                if v5 & 1 << v7:
                    v8 = v5 ^ 1 << v7
                    v9 = (a1[v7] + v6 - 1) // v6
                    v4[v5] = min(v4[v5], v4[v8] + v9)
        return int(v4[v2 - 1])
