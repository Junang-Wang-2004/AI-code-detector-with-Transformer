class C1:

    def cheapestJump(self, a1, a2):
        if not a1 or a1[-1] == -1:
            return []
        v1 = len(a1)
        v2 = float('inf')
        v3 = [v2] * v1
        v4 = [-1] * v1
        if a1[0] != -1:
            v3[0] = a1[0]
        for v5 in range(v1):
            if v3[v5] == v2 or a1[v5] == -1:
                continue
            for v6 in range(v5 + 1, min(v1, v5 + a2 + 1)):
                if a1[v6] == -1:
                    continue
                v7 = v3[v5] + a1[v6]
                if v7 < v3[v6]:
                    v3[v6] = v7
                    v4[v6] = v5
        if v3[v1 - 1] == v2:
            return []
        v8 = []
        v9 = v1 - 1
        while v9 != -1:
            v8.append(v9 + 1)
            v9 = v4[v9]
        v8.reverse()
        return v8
