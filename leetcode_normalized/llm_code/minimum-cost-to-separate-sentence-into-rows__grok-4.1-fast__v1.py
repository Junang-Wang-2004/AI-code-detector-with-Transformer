class C1:

    def minimumCost(self, a1, a2):
        v1 = a1.split()
        if not v1:
            return 0
        v2 = [len(w) for v3 in v1]
        v4 = len(v2)
        v5 = [float('inf')] * (v4 + 1)
        v5[0] = 0
        for v6 in range(1, v4 + 1):
            v5[v6] = float('inf')
            v7 = 0
            for v8 in range(v6 - 1, -1, -1):
                v7 += v2[v8]
                if v8 < v6 - 1:
                    v7 += 1
                if v7 > a2:
                    break
                v9 = (a2 - v7) ** 2
                v5[v6] = min(v5[v6], v5[v8] + v9)
        v10 = float('inf')
        v7 = 0
        for v8 in range(v4 - 1, -1, -1):
            v7 += v2[v8]
            if v8 < v4 - 1:
                v7 += 1
            if v7 > a2:
                break
            v10 = min(v10, v5[v8])
        return int(v10)
