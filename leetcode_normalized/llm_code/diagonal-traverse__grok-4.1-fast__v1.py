class C1:

    def findDiagonalOrder(self, a1):
        if not a1 or not a1[0]:
            return []
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in range(v1 + v2 - 1):
            v5 = [a1[i][v4 - i] for v6 in range(max(0, v4 - v2 + 1), min(v4, v1 - 1) + 1)]
            if v4 % 2 == 0:
                v5.reverse()
            v3.extend(v5)
        return v3
