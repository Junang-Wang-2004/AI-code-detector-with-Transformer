class C1:

    def eliminateMaximum(self, a1, a2):
        v1 = len(a1)
        v2 = sorted(((d - 1) // s for v3, v4 in zip(a1, a2)))
        v5, v6 = (0, v1)
        while v5 < v6:
            v7 = (v5 + v6) // 2
            if v7 < len(v2) and v7 <= v2[v7]:
                v5 = v7 + 1
            else:
                v6 = v7
        return v5
