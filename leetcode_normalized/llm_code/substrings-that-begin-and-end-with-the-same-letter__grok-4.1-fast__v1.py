class C1:

    def numberOfSubstrings(self, a1):
        v1 = len(a1)
        v2 = {}
        for v3 in a1:
            v2[v3] = v2.get(v3, 0) + 1
        v4 = 0
        for v5 in v2.values():
            v4 += v5 * v5
        return (v4 + v1) // 2
