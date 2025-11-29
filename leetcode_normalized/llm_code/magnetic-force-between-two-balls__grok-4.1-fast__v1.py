class C1:

    def maxDistance(self, a1, a2):
        v1 = sorted(a1)

        def feasible(a1):
            v1 = 1
            v2 = v1[0]
            for v3 in v1[1:]:
                if v3 - v2 >= a1:
                    v1 += 1
                    v2 = v3
            return v1 >= a2
        v2, v3 = (1, v1[-1] - v1[0])
        while v2 < v3:
            v4 = (v2 + v3 + 1) // 2
            if feasible(v4):
                v2 = v4
            else:
                v3 = v4 - 1
        return v2
