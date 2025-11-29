class C1:

    def houseOfCards(self, a1):
        v1 = [0] * (a1 + 1)
        v1[0] = 1
        v2 = (a1 + 1) // 3
        for v3 in range(1, v2 + 1):
            v4 = 3 * v3 - 1
            if v4 > a1:
                continue
            v5 = [0] * (a1 + 1)
            for v6 in range(v4, a1 + 1):
                v5[v6] = v1[v6 - v4]
            for v6 in range(v4, a1 + 1):
                v1[v6] += v5[v6]
        return v1[a1]
