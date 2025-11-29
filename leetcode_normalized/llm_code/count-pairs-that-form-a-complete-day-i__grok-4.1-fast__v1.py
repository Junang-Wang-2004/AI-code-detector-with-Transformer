class C1:

    def countCompleteDayPairs(self, a1):
        v1 = 24
        v2 = [0] * v1
        v3 = 0
        for v4 in a1:
            v5 = v4 % v1
            v6 = (v1 - v5) % v1
            v3 += v2[v6]
            v2[v5] += 1
        return v3
