class C1:

    def minimumIndex(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return -1
        v2 = a1[0]
        v3 = 1
        for v4 in range(1, v1):
            if v3 == 0:
                v2 = a1[v4]
                v3 = 1
            elif a1[v4] == v2:
                v3 += 1
            else:
                v3 -= 1
        v5 = sum((x == v2 for v6 in a1))
        v7 = 0
        for v8 in range(v1):
            if a1[v8] == v2:
                v7 += 1
            v9 = v8 + 1
            v10 = v1 - v9
            v11 = v5 - v7
            if v7 * 2 > v9 and v11 * 2 > v10:
                return v8
        return -1
