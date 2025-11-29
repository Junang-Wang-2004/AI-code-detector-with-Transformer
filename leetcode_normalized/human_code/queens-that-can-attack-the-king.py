class C1(object):

    def queensAttacktheKing(self, a1, a2):
        """
        """
        v1 = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        v2 = []
        v3 = {(i, j) for v4, v5 in a1}
        for v6, v7 in v1:
            for v4 in range(1, 8):
                v8, v9 = (a2[0] + v6 * v4, a2[1] + v7 * v4)
                if (v8, v9) in v3:
                    v2.append([v8, v9])
                    break
        return v2
