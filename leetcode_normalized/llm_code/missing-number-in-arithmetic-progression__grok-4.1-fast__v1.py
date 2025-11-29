class C1:

    def missingNumber(self, a1):
        v1 = len(a1)
        v2 = a1[0]
        v3 = (a1[-1] - v2) // v1
        v4, v5 = (0, v1 - 1)
        while v4 < v5:
            v6 = v4 + (v5 - v4) // 2
            if a1[v6] != v2 + v3 * v6:
                v5 = v6
            else:
                v4 = v6 + 1
        return v2 + v3 * v4
