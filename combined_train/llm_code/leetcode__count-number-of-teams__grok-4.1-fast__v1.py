class C1:

    def numTeams(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v4 = 0
            v5 = 0
            for v6 in range(v3):
                if a1[v6] < a1[v3]:
                    v4 += 1
                else:
                    v5 += 1
            v7 = 0
            v8 = 0
            for v9 in range(v3 + 1, v1):
                if a1[v9] < a1[v3]:
                    v7 += 1
                else:
                    v8 += 1
            v2 += v4 * v8 + v5 * v7
        return v2
