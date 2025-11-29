class C1:

    def numberOfSets(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = a1 + a2 - 1
        v3 = 2 * a2
        if v3 > v2:
            return 0
        v4 = v2 - v3
        if v3 > v4:
            v3 = v4
        v5 = 1
        for v6 in range(1, v3 + 1):
            v5 = v5 * (v2 - v6 + 1) // v6
        return v5 % v1
