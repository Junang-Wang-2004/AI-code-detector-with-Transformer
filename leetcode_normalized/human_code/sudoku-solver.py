class C1(object):

    def solveSudoku(self, a1):

        def isValid(a1, a2, a3):
            for v1 in range(9):
                if v1 != a2 and a1[v1][a3] == a1[a2][a3]:
                    return False
            for v2 in range(9):
                if v2 != a3 and a1[a2][v2] == a1[a2][a3]:
                    return False
            v1 = 3 * (a2 / 3)
            while v1 < 3 * (a2 / 3 + 1):
                v2 = 3 * (a3 / 3)
                while v2 < 3 * (a3 / 3 + 1):
                    if (v1 != a2 or v2 != a3) and a1[v1][v2] == a1[a2][a3]:
                        return False
                    v2 += 1
                v1 += 1
            return True

        def solver(a1):
            for v1 in range(len(a1)):
                for v2 in range(len(a1[0])):
                    if a1[v1][v2] == '.':
                        for v3 in range(9):
                            a1[v1][v2] = chr(ord('1') + v3)
                            if isValid(a1, v1, v2) and solver(a1):
                                return True
                            a1[v1][v2] = '.'
                        return False
            return True
        solver(a1)
