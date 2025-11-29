class C1(object):

    def sumOfPowers(self, a1, a2):
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = v3 = 0
        for v4 in sorted({a1[j] - a1[i] for v5 in range(len(a1)) for v6 in range(v5 + 1, len(a1))}, reverse=True):
            v7 = [[0] * (a2 + 1) for v8 in range(len(a1) + 1)]
            v7[0][0] = 1
            v6 = 0
            for v5 in range(len(a1)):
                v6 = next((v6 for v6 in range(v6, len(a1)) if a1[v5] - a1[v6] < v4), len(a1))
                for v9 in range(1, a2 + 1):
                    v7[v5 + 1][v9] = (v7[v5 + 1][v9] + v7[v6 - 1 + 1][v9 - 1]) % v1
                for v9 in range(a2 + 1):
                    v7[v5 + 1][v9] = (v7[v5 + 1][v9] + v7[v5][v9]) % v1
            v10 = (v7[-1][a2] - v3) % v1
            v2 = (v2 + v4 * v10) % v1
            v3 = v7[-1][a2]
        return v2
