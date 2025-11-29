class C1(object):

    def validTicTacToe(self, a1):
        """
        """

        def win(a1, a2):
            for v1 in range(3):
                if all((a1[v1][j] == a2 for v2 in range(3))):
                    return True
                if all((a1[v2][v1] == a2 for v2 in range(3))):
                    return True
            return a2 == a1[1][1] == a1[0][0] == a1[2][2] or a2 == a1[1][1] == a1[0][2] == a1[2][0]
        v1, v2 = ('X', 'O')
        v3 = sum((row.count(v1) for v4 in a1))
        v5 = sum((v4.count(v2) for v4 in a1))
        if v5 not in {v3 - 1, v3}:
            return False
        if win(a1, v1) and v3 - 1 != v5:
            return False
        if win(a1, v2) and v3 != v5:
            return False
        return True
