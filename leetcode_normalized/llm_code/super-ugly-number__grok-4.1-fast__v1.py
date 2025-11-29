class C1:

    def nthSuperUglyNumber(self, a1, a2):
        v1 = len(a2)
        v2 = [0] * a1
        v2[0] = 1
        v3 = [0] * v1
        for v4 in range(1, a1):
            v5 = min((a2[j] * v2[v3[j]] for v6 in range(v1)))
            v2[v4] = v5
            for v6 in range(v1):
                if a2[v6] * v2[v3[v6]] == v5:
                    v3[v6] += 1
        return v2[-1]
