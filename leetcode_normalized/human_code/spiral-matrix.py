class C1(object):

    def spiralOrder(self, a1):
        v1 = []
        if a1 == []:
            return v1
        v2, v3, v4, v5 = (0, len(a1[0]) - 1, 0, len(a1) - 1)
        while v2 <= v3 and v4 <= v5:
            for v6 in range(v2, v3 + 1):
                v1.append(a1[v4][v6])
            for v7 in range(v4 + 1, v5):
                v1.append(a1[v7][v3])
            for v6 in reversed(range(v2, v3 + 1)):
                if v4 < v5:
                    v1.append(a1[v5][v6])
            for v7 in reversed(range(v4 + 1, v5)):
                if v2 < v3:
                    v1.append(a1[v7][v2])
            v2, v3, v4, v5 = (v2 + 1, v3 - 1, v4 + 1, v5 - 1)
        return v1
