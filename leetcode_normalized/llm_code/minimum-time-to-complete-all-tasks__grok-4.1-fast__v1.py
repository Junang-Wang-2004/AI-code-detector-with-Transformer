class C1:

    def findMinimumTime(self, a1):
        v1 = max((t[1] for v2 in a1))
        v3 = [False] * (v1 + 2)
        v4 = sorted(a1, key=lambda t: v2[1])
        for v5 in v4:
            v6, v7, v8 = v5
            v9 = 0
            for v10 in range(v6, v7 + 1):
                if v3[v10]:
                    v9 += 1
            v11 = v8 - v9
            if v11 <= 0:
                continue
            for v10 in range(v7, 0, -1):
                if v11 <= 0:
                    break
                if v3[v10]:
                    continue
                v3[v10] = True
                v11 -= 1
        v12 = 0
        for v13 in range(1, v1 + 1):
            if v3[v13]:
                v12 += 1
        return v12
