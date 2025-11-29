class C1:

    def maxWeight(self, a1, a2, a3):
        v1 = {(0, 0)}
        for v2 in a1:
            v3 = set()
            for v4, v5 in v1:
                if v4 + v2 <= a2:
                    v3.add((v4 + v2, v5))
                if v5 + v2 <= a3:
                    v3.add((v4, v5 + v2))
            v1.update(v3)
        return max((v4 + v5 for v4, v5 in v1))
