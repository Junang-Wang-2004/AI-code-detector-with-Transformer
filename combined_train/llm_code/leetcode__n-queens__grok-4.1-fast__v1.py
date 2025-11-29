class C1:

    def solveNQueens(self, a1):
        v1 = [['.'] * a1 for v2 in range(a1)]
        v3 = []

        def place_queen(a1):
            if a1 == a1:
                v3.append([''.join(row) for v1 in v1])
                return
            for v2 in range(a1):
                if can_place(a1, v2):
                    v1[a1][v2] = 'Q'
                    place_queen(a1 + 1)
                    v1[a1][v2] = '.'

        def can_place(a1, a2):
            for v1 in range(a1):
                if v1[v1][a2] == 'Q':
                    return False
                v2 = a1 + a2 - v1
                if 0 <= v2 < a1 and v1[v1][v2] == 'Q':
                    return False
                v3 = v1 - a1 + a2
                if 0 <= v3 < a1 and v1[v1][v3] == 'Q':
                    return False
            return True
        place_queen(0)
        return v3
