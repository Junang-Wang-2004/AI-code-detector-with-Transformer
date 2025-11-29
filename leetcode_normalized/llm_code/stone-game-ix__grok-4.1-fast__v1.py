class C1:

    def stoneGameIX(self, a1):
        v1 = [0] * 3
        for v2 in a1:
            v1[v2 % 3] += 1
        v3, v4, v5 = v1
        if v3 % 2 == 0:
            return v4 > 0 and v5 > 0
        return abs(v4 - v5) >= 3
