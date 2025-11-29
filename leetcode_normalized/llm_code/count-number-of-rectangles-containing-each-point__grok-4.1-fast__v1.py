class C1:

    def countRectangles(self, a1, a2):
        if not a1:
            return [0] * len(a2)
        v1 = max((h for v2, v3 in a1))
        v4 = [[] for v2 in range(v1 + 1)]
        for v5, v6 in a1:
            v4[v6].append(v5)
        for v7 in v4:
            v7.sort()

        def num_greater_or_equal(a1, a2):
            v1, v2 = (0, len(a1))
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if a1[v3] >= a2:
                    v2 = v3
                else:
                    v1 = v3 + 1
            return len(a1) - v1
        v8 = []
        for v9, v10 in a2:
            v11 = 0
            for v3 in range(v10, v1 + 1):
                v11 += num_greater_or_equal(v4[v3], v9)
            v8.append(v11)
        return v8
