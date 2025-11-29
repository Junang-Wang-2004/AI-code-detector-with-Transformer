class C1(object):

    def countCornerRectangles(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [[] for v4 in range(v2)]
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6]:
                    v3[v6].append(v5)
        v7 = 0

        def intersect_size(a1, a2):
            v1 = v2 = 0
            v3 = 0
            while v1 < len(a1) and v2 < len(a2):
                if a1[v1] == a2[v2]:
                    v3 += 1
                    v1 += 1
                    v2 += 1
                elif a1[v1] < a2[v2]:
                    v1 += 1
                else:
                    v2 += 1
            return v3
        for v8 in range(v2):
            for v9 in range(v8):
                v10 = intersect_size(v3[v8], v3[v9])
                v7 += v10 * (v10 - 1) // 2
        return v7
