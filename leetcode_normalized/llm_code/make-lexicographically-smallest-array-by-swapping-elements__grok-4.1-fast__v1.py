class C1:

    def lexicographicallySmallestArray(self, a1, a2):
        v1 = len(a1)
        v2 = [(a1[i], i) for v3 in range(v1)]
        v2.sort()
        v4 = [0] * v1
        v3 = 0
        while v3 < v1:
            v5 = v3
            while v5 + 1 < v1 and v2[v5 + 1][0] - v2[v5][0] <= a2:
                v5 += 1
            v6 = sorted((v2[k][1] for v7 in range(v3, v5 + 1)))
            for v7 in range(v5 - v3 + 1):
                v4[v6[v7]] = v2[v3 + v7][0]
            v3 = v5 + 1
        return v4
