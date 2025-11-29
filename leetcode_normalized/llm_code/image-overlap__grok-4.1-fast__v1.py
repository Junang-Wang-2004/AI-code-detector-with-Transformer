class C1:

    def largestOverlap(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        for v3 in range(1 - v1, v1):
            for v4 in range(1 - v1, v1):
                v5 = 0
                for v6 in range(v1):
                    v7 = v6 - v3
                    if not 0 <= v7 < v1:
                        continue
                    for v8 in range(v1):
                        v9 = v8 - v4
                        if 0 <= v9 < v1 and a1[v6][v8] and a2[v7][v9]:
                            v5 += 1
                v2 = max(v2, v5)
        return v2
