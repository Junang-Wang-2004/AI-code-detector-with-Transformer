class C1:

    def maxPower(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = min((v2[min(v1, v3 + a2 + 1)] - v2[max(0, v3 - a2)] for v3 in range(v1)))

        def feasible(a1):
            v1 = list(a1)
            v2 = a3
            v3 = min(v1 - 1, a2)
            v4 = sum(v1[:v3 + 1])
            for v5 in range(v1):
                if v4 < a1:
                    v6 = a1 - v4
                    if v6 > v2:
                        return False
                    v2 -= v6
                    v4 += v6
                    v7 = min(v1 - 1, v5 + a2)
                    v1[v7] += v6
                if v5 == v1 - 1:
                    break
                v8 = max(0, v5 - a2)
                v9 = max(0, v5 + 1 - a2)
                v10 = min(v1 - 1, v5 + a2)
                v11 = min(v1 - 1, v5 + 1 + a2)
                if v9 > v8:
                    v4 -= v1[v8]
                if v11 > v10:
                    v4 += v1[v11]
            return True
        v5, v6 = (v4, v4 + a3)
        while v5 < v6:
            v7 = (v5 + v6 + 1) // 2
            if feasible(v7):
                v5 = v7
            else:
                v6 = v7 - 1
        return v5
