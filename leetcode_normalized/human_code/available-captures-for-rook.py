class C1(object):

    def numRookCaptures(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2, v3 = (None, None)
        for v4 in range(8):
            if v2 is not None:
                break
            for v5 in range(8):
                if a1[v4][v5] == 'R':
                    v2, v3 = (v4, v5)
                    break
        v6 = 0
        for v7 in v1:
            v8, v9 = (v2 + v7[0], v3 + v7[1])
            while 0 <= v8 < 8 and 0 <= v9 < 8:
                if a1[v8][v9] == 'p':
                    v6 += 1
                if a1[v8][v9] != '.':
                    break
                v8, v9 = (v8 + v7[0], v9 + v7[1])
        return v6
