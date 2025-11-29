class C1:

    def maximumSumOfHeights(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = [-1]
        v4 = 0
        for v5 in range(v1):
            while len(v3) > 1 and a1[v3[-1]] >= a1[v5]:
                v6 = v3.pop()
                v4 -= (v6 - v3[-1]) * a1[v6]
            v4 += (v5 - v3[-1]) * a1[v5]
            v3.append(v5)
            v2[v5] = v4
        v7 = [0] * v1
        v3 = [v1]
        v4 = 0
        for v5 in range(v1 - 1, -1, -1):
            while len(v3) > 1 and a1[v3[-1]] >= a1[v5]:
                v6 = v3.pop()
                v4 -= (v3[-1] - v6) * a1[v6]
            v4 += (v3[-1] - v5) * a1[v5]
            v3.append(v5)
            v7[v5] = v4
        v8 = 0
        for v5 in range(v1):
            v8 = max(v8, v2[v5] + v7[v5] - a1[v5])
        return v8
