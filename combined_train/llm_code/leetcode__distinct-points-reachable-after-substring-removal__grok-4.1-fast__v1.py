class C1:

    def distinctPoints(self, a1, a2):

        def delta(a1):
            if a1 == 'U':
                return (0, 1)
            if a1 == 'D':
                return (0, -1)
            if a1 == 'L':
                return (-1, 0)
            return (1, 0)
        v1 = []
        v2 = len(a1)
        for v3 in range(a2, v2):
            v4, v5 = delta(a1[v3])
            v6, v7 = delta(a1[v3 - a2])
            v1.append((v4 - v6, v5 - v7))
        v8 = set()
        v9, v10 = (0, 0)
        v8.add((v9, v10))
        for v11, v12 in v1:
            v9 += v11
            v10 += v12
            v8.add((v9, v10))
        return len(v8)
