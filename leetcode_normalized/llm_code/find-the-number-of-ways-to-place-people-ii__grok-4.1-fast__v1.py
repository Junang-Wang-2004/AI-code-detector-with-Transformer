class C1:

    def numberOfPairs(self, a1):
        v1 = sorted(a1, key=lambda p: (p[0], -p[1]))
        v2 = [pt[1] for v3 in v1]
        v4 = len(v2)
        v5 = 0
        for v6 in range(v4):
            v7 = float('-inf')
            for v8 in range(v6 + 1, v4):
                if v2[v6] < v2[v8]:
                    continue
                if v2[v8] > v7:
                    v7 = v2[v8]
                    v5 += 1
        return v5
