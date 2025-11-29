class C1:

    def minimizedMaximum(self, a1, a2):
        v1, v2 = (1, max(a2))
        while v1 < v2:
            v3 = (v1 + v2) // 2
            v4 = 0
            for v5 in a2:
                v4 += (v5 - 1) // v3 + 1
            if v4 <= a1:
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
