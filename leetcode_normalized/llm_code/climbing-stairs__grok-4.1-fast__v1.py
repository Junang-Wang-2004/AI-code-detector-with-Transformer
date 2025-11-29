class C1:

    def climbStairs(self, a1):
        if a1 < 2:
            return 1
        v1 = 1
        v2 = 2
        for v3 in range(3, a1 + 1):
            v4 = v1 + v2
            v1 = v2
            v2 = v4
        return v2
