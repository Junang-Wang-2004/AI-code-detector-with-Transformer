class C1:

    def minWastedSpace(self, a1, a2):
        v1 = sorted(a1)
        v2 = len(v1)
        if v2 == 0:
            return 0
        v3 = 10 ** 9 + 7
        v4 = float('inf')
        v5 = v1[-1]
        for v6 in a2:
            v7 = sorted(v6)
            if not v7 or v7[-1] < v5:
                continue
            v8 = 0
            v9 = 0
            for v10 in v7:
                while v8 < v2 and v1[v8] <= v10:
                    v9 += v10 - v1[v8]
                    v8 += 1
                if v8 == v2:
                    break
            if v8 == v2:
                v4 = min(v4, v9)
        return v4 % v3 if v4 != float('inf') else -1
