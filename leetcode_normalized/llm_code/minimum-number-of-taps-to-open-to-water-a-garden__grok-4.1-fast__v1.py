class C1:

    def minTaps(self, a1, a2):
        v1 = [0] * (a1 + 1)
        for v2, v3 in enumerate(a2):
            v4 = max(0, v2 - v3)
            v5 = min(a1, v2 + v3)
            v1[v4] = max(v1[v4], v5)
        v6 = 0
        v7 = 0
        v8 = 0
        for v9 in range(a1 + 1):
            if v9 > v6:
                return -1
            v6 = max(v6, v1[v9])
            if v9 == v7:
                v8 += 1
                v7 = v6
                if v7 >= a1:
                    return v8
        return v8
