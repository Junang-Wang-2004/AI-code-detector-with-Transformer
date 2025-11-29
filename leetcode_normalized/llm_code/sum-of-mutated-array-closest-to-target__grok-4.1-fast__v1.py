class C1:

    def findBestValue(self, a1, a2):
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = a2
        v4 = 0
        while v4 < v2 and v1[v4] * (v2 - v4) <= v3:
            v3 -= v1[v4]
            v4 += 1
        if v4 == v2:
            return v1[-1]
        v5 = v2 - v4
        v6 = v3 // v5
        v7 = v3 % v5
        return v6 if 2 * v7 <= v5 else v6 + 1
