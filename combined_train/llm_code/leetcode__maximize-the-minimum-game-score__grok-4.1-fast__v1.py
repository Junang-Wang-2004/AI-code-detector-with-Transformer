class C1:

    def maxScore(self, a1, a2):
        v1 = max(a1)
        v2 = 0
        v3 = v1 * a2
        while v2 < v3:
            v4 = v2 + (v3 - v2 + 1) // 2
            v5 = 0
            v6 = 0
            v7 = len(a1)
            v8 = True
            for v9 in range(v7):
                v10 = a1[v9]
                v11 = (v4 + v10 - 1) // v10
                v12 = v11 - v6
                if v12 >= 1:
                    v5 += 2 * v12 - 1
                    v6 = v12 - 1
                elif v9 < v7 - 1:
                    v5 += 1
                    v6 = 0
                if v5 > a2:
                    v8 = False
                    break
            if v8:
                v2 = v4
            else:
                v3 = v4 - 1
        return v2
