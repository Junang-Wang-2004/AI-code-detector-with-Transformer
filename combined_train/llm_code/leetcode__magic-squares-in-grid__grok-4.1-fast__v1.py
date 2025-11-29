class C1:

    def numMagicSquaresInside(self, a1):

        def check_magic(a1, a2):
            v1 = 15
            v2 = range(3)
            v3 = [sum((a1[a1 + x][a2 + y] for v4 in v2)) for v5 in v2]
            if any((total != v1 for v6 in v3)):
                return False
            v7 = [sum((a1[a1 + v5][a2 + v4] for v5 in v2)) for v4 in v2]
            if any((v6 != v1 for v6 in v7)):
                return False
            v8 = sum((a1[a1 + v5][a2 + v5] for v5 in v2))
            v9 = sum((a1[a1 + v5][a2 + 2 - v5] for v5 in v2))
            if v8 != v1 or v9 != v1:
                return False
            v10 = [a1[a1 + v5][a2 + v4] for v5 in v2 for v4 in v2]
            return sorted(v10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        for v4 in range(v1 - 2):
            for v5 in range(v2 - 2):
                if check_magic(v4, v5):
                    v3 += 1
        return v3
