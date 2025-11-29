class C1:

    def findTheString(self, a1):
        v1 = len(a1)
        v2 = list(range(v1))
        v3 = [0] * v1

        def find(a1):
            if v2[a1] != a1:
                v2[a1] = find(v2[a1])
            return v2[a1]

        def unite(a1, a2):
            v1 = find(a1)
            v2 = find(a2)
            if v1 == v2:
                return
            if v3[v1] < v3[v2]:
                v2[v1] = v2
            elif v3[v1] > v3[v2]:
                v2[v2] = v1
            else:
                v2[v2] = v1
                v3[v1] += 1
        for v4 in range(v1):
            for v5 in range(v4 + 1, v1):
                if a1[v4][v5] > 0:
                    unite(v4, v5)
        v6 = set((find(v4) for v4 in range(v1)))
        if len(v6) > 26:
            return ''
        v7 = {}
        v8 = 0
        v9 = [0] * v1
        for v4 in range(v1):
            v10 = find(v4)
            if v10 not in v7:
                v7[v10] = v8
                v8 += 1
            v9[v4] = v7[v10]
        for v4 in range(v1 - 1, -1, -1):
            for v5 in range(v1 - 1, -1, -1):
                if v9[v4] == v9[v5]:
                    v11 = 1 + (a1[v4 + 1][v5 + 1] if v4 + 1 < v1 and v5 + 1 < v1 else 0)
                else:
                    v11 = 0
                if v11 != a1[v4][v5]:
                    return ''
        return ''.join((chr(ord('a') + c) for v12 in v9))
