class C1:

    def minimumTimeToInitialState(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = 0
        v4 = 0
        for v5 in range(1, v1):
            if v5 <= v4:
                v2[v5] = min(v4 - v5 + 1, v2[v5 - v3])
            while v5 + v2[v5] < v1 and a1[v2[v5]] == a1[v5 + v2[v5]]:
                v2[v5] += 1
            if v5 + v2[v5] - 1 > v4:
                v3 = v5
                v4 = v5 + v2[v5] - 1
        v6 = 1
        while v6 * a2 < v1:
            v7 = v6 * a2
            v8 = v1 - v7
            if v2[v7] >= v8:
                return v6
            v6 += 1
        return v6
