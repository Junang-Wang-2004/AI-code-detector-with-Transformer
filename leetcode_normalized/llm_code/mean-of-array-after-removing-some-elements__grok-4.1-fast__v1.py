class C1:

    def trimMean(self, a1):
        v1 = len(a1)
        v2 = v1 // 20
        v3 = sorted(a1)
        v4 = sum(v3[v2:v1 - v2])
        v5 = v1 - 2 * v2
        return v4 / v5
