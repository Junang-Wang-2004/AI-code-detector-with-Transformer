class C1:

    def minimumSize(self, a1, a2):

        def feasible(a1, a2, a3):
            return sum(((n - 1) // a3 for v1 in a1)) <= a2
        v1 = 1
        v2 = max(a1)
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if feasible(a1, a2, v3):
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
