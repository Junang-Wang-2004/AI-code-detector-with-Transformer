class C1:

    def projectionArea(self, a1):
        v1 = sum((1 for v2 in a1 for v3 in v2 if v3))
        v4 = sum((max(v2) for v2 in a1))
        v5 = sum((max(col) for v6 in zip(*a1)))
        return v1 + v4 + v5
