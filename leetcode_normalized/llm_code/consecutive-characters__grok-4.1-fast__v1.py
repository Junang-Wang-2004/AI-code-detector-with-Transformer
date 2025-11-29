class C1:

    def maxPower(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = 1
        v3 = 0
        for v4 in range(1, v1):
            if a1[v4] != a1[v4 - 1]:
                v2 = max(v2, v4 - v3)
                v3 = v4
        return max(v2, v1 - v3)
