class C1:

    def maxNumberOfAlloys(self, a1, a2, a3, a4, a5, a6):
        v1 = sum(a5)
        v2 = v1 + a3 + 1
        v3 = 0
        for v4 in a4:
            v5 = 0
            v6 = v2
            while v5 < v6:
                v7 = (v5 + v6 + 1) // 2
                v8 = 0
                v9 = True
                for v10 in range(a1):
                    v11 = v7 * v4[v10] - a5[v10]
                    if v11 > 0:
                        v8 += v11 * a6[v10]
                        if v8 > a3:
                            v9 = False
                            break
                if v9:
                    v5 = v7
                else:
                    v6 = v7 - 1
            v3 = max(v3, v5)
        return v3
