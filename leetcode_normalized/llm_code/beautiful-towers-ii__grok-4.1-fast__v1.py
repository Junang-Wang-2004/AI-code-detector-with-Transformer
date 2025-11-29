class C1(object):

    def maximumSumOfHeights(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = [-1]
        v4 = 0
        for v5 in range(v1):
            while len(v3) > 1 and a1[v3[-1]] >= a1[v5]:
                v6 = v3.pop()
                v4 -= a1[v6] * (v6 - v3[-1])
            v7 = v5 - v3[-1]
            v4 += a1[v5] * v7
            v3.append(v5)
            v2[v5] = v4
        v8 = [0] * v1
        v3 = [v1]
        v9 = 0
        for v10 in range(v1 - 1, -1, -1):
            while len(v3) > 1 and a1[v3[-1]] >= a1[v10]:
                v6 = v3.pop()
                v9 -= a1[v6] * (v3[-1] - v6)
            v7 = v3[-1] - v10
            v9 += a1[v10] * v7
            v3.append(v10)
            v8[v10] = v9
        v11 = 0
        for v5 in range(v1):
            v11 = max(v11, v2[v5] + v8[v5] - a1[v5])
        return v11
