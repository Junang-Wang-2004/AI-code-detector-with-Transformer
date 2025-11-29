class C1:

    def findDiagonalOrder(self, a1):
        v1 = []
        for v2, v3 in enumerate(a1):
            for v4, v5 in enumerate(v3):
                v1.append((v2 + v4, -v2, v5))
        v1.sort()
        return [v for v6, v6, v7 in v1]
