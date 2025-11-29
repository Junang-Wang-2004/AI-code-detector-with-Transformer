class C1:

    def minimumReplacement(self, a1):
        v1 = 0
        v2 = a1[-1]
        for v3 in range(len(a1) - 2, -1, -1):
            v4 = a1[v3]
            v5 = (v4 + v2 - 1) // v2
            v1 += v5 - 1
            v2 = v4 // v5
        return v1
