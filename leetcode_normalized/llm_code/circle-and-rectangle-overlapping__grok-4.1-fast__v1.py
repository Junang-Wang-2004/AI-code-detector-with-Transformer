class C1:

    def checkOverlap(self, a1, a2, a3, a4, a5, a6, a7):
        v1 = a4 - a2
        v2 = a6 - a2
        v3 = a5 - a3
        v4 = a7 - a3
        v5 = max(v1, min(0, v2))
        v6 = max(v3, min(0, v4))
        return v5 * v5 + v6 * v6 <= a1 * a1
