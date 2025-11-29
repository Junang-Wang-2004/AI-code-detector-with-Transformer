class C1:

    def maximumCandies(self, a1, a2):

        def feasible(a1):
            v1 = 0
            for v2 in a1:
                v1 += v2 // a1
            return v1 >= a2
        v1 = 1
        v2 = max(a1)
        while v1 < v2:
            v3 = (v1 + v2 + 1) // 2
            if feasible(v3):
                v1 = v3
            else:
                v2 = v3 - 1
        return v1
