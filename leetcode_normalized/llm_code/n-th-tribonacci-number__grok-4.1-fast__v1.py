class C1:

    def tribonacci(self, a1):
        if a1 == 0:
            return 0
        if a1 < 3:
            return 1
        v1, v2, v3 = (0, 1, 1)
        for v4 in range(a1 - 2):
            v5 = v1 + v2 + v3
            v1, v2, v3 = (v2, v3, v5)
        return v3
