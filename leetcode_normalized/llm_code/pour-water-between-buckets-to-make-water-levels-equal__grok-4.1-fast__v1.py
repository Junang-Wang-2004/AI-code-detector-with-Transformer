class C1:

    def equalizeWater(self, a1, a2):
        v1 = (100 - a2) / 100

        def feasible(a1):
            v1 = sum((max(b - a1, 0) for v2 in a1))
            v3 = sum((max(a1 - v2, 0) for v2 in a1))
            return v1 * v1 >= v3
        v2 = min(a1)
        v3 = sum(a1) / len(a1)
        while v3 - v2 > 1e-09:
            v4 = (v2 + v3) / 2
            if feasible(v4):
                v2 = v4
            else:
                v3 = v4
        return v2
