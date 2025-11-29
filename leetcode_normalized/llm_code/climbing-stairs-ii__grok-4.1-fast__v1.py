class C1:

    def climbStairs(self, a1, a2):
        if a1 == 0:
            return 0
        v1 = [float('inf'), float('inf'), 0]
        v2 = [9, 4, 1]
        for v3 in range(a1):
            v4 = a2[v3] + min((v1[k] + v2[k] for v5 in range(3)))
            v1 = v1[1:] + [v4]
        return v1[-1]
