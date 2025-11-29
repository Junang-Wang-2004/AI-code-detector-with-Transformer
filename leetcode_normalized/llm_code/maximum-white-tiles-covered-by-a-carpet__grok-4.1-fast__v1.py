class C1:

    def maximumWhiteTiles(self, a1, a2):
        a1.sort(key=lambda t: t[0])
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + (a1[v3][1] - a1[v3][0] + 1)
        v4 = 0
        v5 = -1
        for v3 in range(v1):
            v6 = a1[v3][0] + a2 - 1
            while v5 + 1 < v1 and a1[v5 + 1][0] <= v6:
                v5 += 1
            if v5 >= v3:
                v7 = max(a1[v5][1] - v6, 0)
                v8 = v2[v5 + 1] - v2[v3] - v7
                if v8 > v4:
                    v4 = v8
        return v4
