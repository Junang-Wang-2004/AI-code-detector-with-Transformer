class C1:

    def ways(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2, v3 = (len(a1), len(a1[0]))
        v4 = [[0] * (v3 + 1) for v5 in range(v2 + 1)]
        for v6 in range(v2 - 1, -1, -1):
            for v7 in range(v3 - 1, -1, -1):
                v4[v6][v7] = v4[v6][v7 + 1] + v4[v6 + 1][v7] - v4[v6 + 1][v7 + 1] + (1 if a1[v6][v7] == 'A' else 0)
        v8 = [[[-1] * a2 for v5 in range(v3)] for v5 in range(v2)]

        def count_ways(a1, a2, a3):
            if a3 == 0:
                return 1 if v4[a1][a2] > 0 else 0
            if v8[a1][a2][a3] != -1:
                return v8[a1][a2][a3]
            v1 = 0
            for v2 in range(a1 + 1, v2):
                if v4[a1][a2] > v4[v2][a2]:
                    v1 = (v1 + count_ways(v2, a2, a3 - 1)) % v1
                if v4[v2][a2] == 0:
                    break
            for v3 in range(a2 + 1, v3):
                if v4[a1][a2] > v4[a1][v3]:
                    v1 = (v1 + count_ways(a1, v3, a3 - 1)) % v1
                if v4[a1][v3] == 0:
                    break
            v8[a1][a2][a3] = v1
            return v1
        return count_ways(0, 0, a2 - 1)
