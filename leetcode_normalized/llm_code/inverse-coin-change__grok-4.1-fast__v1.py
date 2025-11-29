class C1:

    def findCoins(self, a1):
        v1 = []
        v2 = len(a1)
        v3 = [1] + [0] * v2
        for v4 in range(1, v2 + 1):
            v5 = a1[v4 - 1] - v3[v4]
            if v5 == 1:
                v1.append(v4)
                for v6 in range(v4, v2 + 1):
                    v3[v6] += v3[v6 - v4]
            if a1[v4 - 1] != v3[v4]:
                return []
        return v1
