class C1:

    def solveSudoku(self, a1):
        v1 = [0] * 9
        v2 = [0] * 9
        v3 = [0] * 9
        v4 = []
        for v5 in range(9):
            for v6 in range(9):
                v7 = a1[v5][v6]
                if v7 == '.':
                    v4.append((v5, v6))
                else:
                    v8 = 1 << int(v7) - 1
                    v1[v5] |= v8
                    v2[v6] |= v8
                    v3[v5 // 3 * 3 + v6 // 3] |= v8

        def search(a1):
            if a1 == len(v4):
                return True
            v1, v2 = v4[a1]
            v3 = v1 // 3 * 3 + v2 // 3
            for v4 in range(9):
                v5 = 1 << v4
                if v1[v1] & v5 == 0 and v2[v2] & v5 == 0 and (v3[v3] & v5 == 0):
                    a1[v1][v2] = str(v4 + 1)
                    v1[v1] |= v5
                    v2[v2] |= v5
                    v3[v3] |= v5
                    if search(a1 + 1):
                        return True
                    a1[v1][v2] = '.'
                    v1[v1] &= ~v5
                    v2[v2] &= ~v5
                    v3[v3] &= ~v5
            return False
        search(0)
