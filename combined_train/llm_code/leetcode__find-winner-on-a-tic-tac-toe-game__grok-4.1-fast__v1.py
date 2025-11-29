class C1:

    def tictactoe(self, a1):
        v1 = [0] * 3
        v2 = [0] * 3
        v3 = 0
        v4 = 0
        v5 = [0] * 3
        v6 = [0] * 3
        v7 = 0
        v8 = 0
        v9 = 'A'
        for v10, v11 in a1:
            if v9 == 'A':
                v1[v10] += 1
                v2[v11] += 1
                if v10 == v11:
                    v3 += 1
                if v10 + v11 == 2:
                    v4 += 1
                if v1[v10] == 3 or v2[v11] == 3 or v3 == 3 or (v4 == 3):
                    return 'A'
            else:
                v5[v10] += 1
                v6[v11] += 1
                if v10 == v11:
                    v7 += 1
                if v10 + v11 == 2:
                    v8 += 1
                if v5[v10] == 3 or v6[v11] == 3 or v7 == 3 or (v8 == 3):
                    return 'B'
            v9 = 'B' if v9 == 'A' else 'A'
        return 'Draw' if len(a1) == 9 else 'Pending'
