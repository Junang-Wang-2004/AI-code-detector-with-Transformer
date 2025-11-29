class C1:

    def countOfPairs(self, a1, a2, a3):
        a2 -= 1
        a3 -= 1
        v3 = [0] * a1
        for v4 in range(a1):
            for v5 in range(a1):
                if v4 == v5:
                    continue
                v6 = abs(v4 - v5)
                v7 = abs(v4 - a2) + 1 + abs(v5 - a3)
                v8 = abs(v4 - a3) + 1 + abs(v5 - a2)
                v9 = min(v6, v7, v8)
                v3[v9 - 1] += 1
        return v3
