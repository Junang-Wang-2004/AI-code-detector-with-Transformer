class C1(object):

    def minCost(self, a1, a2):
        v1 = len(a1)
        v2 = float('inf')
        v3 = [v2] * (v1 + 1)
        v3[0] = 0
        for v4 in range(1, v1 + 1):
            v5 = [0] * v1
            v6 = 0
            for v7 in range(v4 - 1, -1, -1):
                v8 = a1[v7]
                v5[v8] += 1
                if v5[v8] == 1:
                    v6 += 1
                elif v5[v8] == 2:
                    v6 -= 1
                v9 = v4 - v7
                v10 = a2 + v9 - v6
                v3[v4] = min(v3[v4], v3[v7] + v10)
        return v3[v1]
