class C1:

    def numWays(self, a1, a2):
        if a1 == 0:
            return 0
        if a1 == 1:
            return a2
        if a1 == 2:
            return a2 * a2
        v1 = a2
        v2 = a2 * a2
        for v3 in range(3, a1 + 1):
            v4 = (a2 - 1) * (v1 + v2)
            v1 = v2
            v2 = v4
        return v2
