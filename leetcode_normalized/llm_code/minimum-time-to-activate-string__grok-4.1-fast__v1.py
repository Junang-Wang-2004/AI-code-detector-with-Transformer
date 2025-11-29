class C1:

    def minTime(self, a1, a2, a3):
        v1 = len(a1)
        v2 = v1 * (v1 + 1) // 2
        if v2 < a3:
            return -1
        v3 = len(a2)
        v4 = [-1] + list(range(v1 - 1))
        v5 = list(range(1, v1 + 1))
        v6 = 0
        while v6 < v3:
            v7 = a2[v3 - 1 - v6]
            v8 = v4[v7]
            v9 = v5[v7]
            v10 = (v7 - v8) * (v9 - v7)
            v2 -= v10
            if v2 < a3:
                return v3 - 1 - v6
            if v8 >= 0:
                v5[v8] = v9
            if v9 < v1:
                v4[v9] = v8
            v6 += 1
        return 0
