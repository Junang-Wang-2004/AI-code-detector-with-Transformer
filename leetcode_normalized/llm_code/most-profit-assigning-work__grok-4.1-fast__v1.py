class C1(object):

    def maxProfitAssignment(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [(a1[idx], a2[idx]) for v3 in range(v1)]
        v2.sort(key=lambda tp: tp[0])
        if v1 == 0:
            return 0
        v4 = [0] * v1
        v4[0] = v2[0][1]
        for v5 in range(1, v1):
            v4[v5] = max(v4[v5 - 1], v2[v5][1])
        v6 = 0
        for v7 in a3:
            v8, v9 = (0, v1 - 1)
            v10 = -1
            while v8 <= v9:
                v11 = (v8 + v9) // 2
                if v2[v11][0] <= v7:
                    v10 = v11
                    v8 = v11 + 1
                else:
                    v9 = v11 - 1
            if v10 >= 0:
                v6 += v4[v10]
        return v6
