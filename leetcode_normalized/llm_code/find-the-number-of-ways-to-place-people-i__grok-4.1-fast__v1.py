class C1:

    def numberOfPairs(self, a1):
        v1 = len(a1)
        v2 = sorted(range(v1), key=lambda idx: (a1[idx][0], -a1[idx][1]))
        v3 = 0
        for v4 in range(v1):
            v5 = float('-inf')
            v6 = a1[v2[v4]][1]
            for v7 in range(v4 + 1, v1):
                v8 = a1[v2[v7]][1]
                if v6 < v8:
                    continue
                if v8 > v5:
                    v5 = v8
                    v3 += 1
        return v3
