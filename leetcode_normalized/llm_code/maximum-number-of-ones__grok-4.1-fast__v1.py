class C1:

    def maximumNumberOfOnes(self, a1, a2, a3, a4):
        v1, v2 = divmod(a2, a3)
        v3, v4 = divmod(a1, a3)
        v5 = [((v1 + 1) * (v3 + 1), v2 * v4), ((v1 + 1) * v3, v2 * (a3 - v4)), (v1 * (v3 + 1), (a3 - v2) * v4), (v1 * v3, (a3 - v2) * (a3 - v4))]
        v5.sort(key=lambda x: x[0], reverse=True)
        v6 = 0
        v7 = a4
        for v8, v9 in v5:
            if v7 == 0:
                break
            v10 = min(v7, v9)
            v6 += v10 * v8
            v7 -= v10
        return v6
