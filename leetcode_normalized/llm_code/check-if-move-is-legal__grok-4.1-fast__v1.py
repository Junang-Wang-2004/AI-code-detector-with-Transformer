class C1(object):

    def checkMove(self, a1, a2, a3, a4):
        v1 = len(a1)
        v2 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for v3, v4 in v2:
            v5, v6 = (a2 + v3, a3 + v4)
            v7 = 0
            while 0 <= v5 < v1 and 0 <= v6 < v1 and (a1[v5][v6] != '.') and (a1[v5][v6] != a4):
                v7 += 1
                v5 += v3
                v6 += v4
            if v7 > 0 and 0 <= v5 < v1 and (0 <= v6 < v1) and (a1[v5][v6] == a4):
                return True
        return False
