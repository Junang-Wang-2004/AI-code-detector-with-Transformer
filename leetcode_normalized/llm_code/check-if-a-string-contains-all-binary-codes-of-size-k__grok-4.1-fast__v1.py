class C1:

    def hasAllCodes(self, a1, a2):
        v1 = len(a1)
        v2 = 1 << a2
        if v1 < v2:
            return False
        v3 = [False] * v2
        v4 = 0
        for v5 in range(a2):
            v4 = v4 << 1 | int(a1[v5])
        v3[v4] = True
        v6 = v2 - 1
        for v7 in range(1, v1 - a2 + 1):
            v4 = v4 << 1 & v6 | int(a1[v7 + a2 - 1])
            v3[v4] = True
        return all(v3)
