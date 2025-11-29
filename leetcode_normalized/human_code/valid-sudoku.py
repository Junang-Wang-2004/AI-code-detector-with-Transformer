class C1(object):

    def isValidSudoku(self, a1):
        """
        """
        for v1 in range(9):
            if not self.isValidList([a1[v1][j] for v2 in range(9)]) or not self.isValidList([a1[v2][v1] for v2 in range(9)]):
                return False
        for v1 in range(3):
            for v2 in range(3):
                if not self.isValidList([a1[m][n] for v3 in range(3 * v2, 3 * v2 + 3) for v4 in range(3 * v1, 3 * v1 + 3)]):
                    return False
        return True

    def isValidList(self, a1):
        a1 = [x for v2 in a1 if v2 != '.']
        return len(set(a1)) == len(a1)
