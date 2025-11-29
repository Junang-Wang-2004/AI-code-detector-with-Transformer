class C1:

    def minOperations(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        if v1 > 6 * v2 or v2 > 6 * v1:
            return -1
        v3 = sum(a1)
        v4 = sum(a2)
        if v3 > v4:
            a1, a2 = (a2, a1)
            v3, v4 = (v4, v3)
        v7 = v4 - v3
        v8 = []
        for v9 in a1:
            v8.append(6 - v9)
        for v9 in a2:
            v8.append(v9 - 1)
        v8.sort(reverse=True)
        v10 = 0
        for v11 in v8:
            if v7 <= 0:
                break
            if v11 > 0:
                v12 = min(v11, v7)
                v7 -= v12
                v10 += 1
        return v10
