class C1(object):

    def spiralOrder(self, a1):
        if not a1 or not a1[0]:
            return []
        v1 = []
        v2, v3 = (len(a1), len(a1[0]))
        v4, v5 = (0, v2 - 1)
        v6, v7 = (0, v3 - 1)
        while v4 <= v5 and v6 <= v7:
            for v8 in range(v6, v7 + 1):
                v1.append(a1[v4][v8])
            v4 += 1
            for v9 in range(v4, v5 + 1):
                v1.append(a1[v9][v7])
            v7 -= 1
            if v4 <= v5:
                for v8 in range(v7, v6 - 1, -1):
                    v1.append(a1[v5][v8])
                v5 -= 1
            if v6 <= v7:
                for v9 in range(v5, v4 - 1, -1):
                    v1.append(a1[v9][v6])
                v6 += 1
        return v1
