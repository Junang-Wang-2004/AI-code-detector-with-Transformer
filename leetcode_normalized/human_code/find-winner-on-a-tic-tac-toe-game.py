class C1(object):

    def tictactoe(self, a1):
        """
        """
        v1, v2 = ([[0] * 3 for v3 in range(2)], [[0] * 3 for v3 in range(2)])
        v4, v5 = ([0] * 2, [0] * 2)
        v6 = 0
        for v7, v8 in a1:
            v1[v6][v7] += 1
            v2[v6][v8] += 1
            v4[v6] += v7 == v8
            v5[v6] += v7 + v8 == 2
            if 3 in (v1[v6][v7], v2[v6][v8], v4[v6], v5[v6]):
                return 'AB'[v6]
            v6 ^= 1
        return 'Draw' if len(a1) == 9 else 'Pending'
