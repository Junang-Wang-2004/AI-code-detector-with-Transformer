class C1(object):

    def candyCrush(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = True
        while v3:
            v3 = False
            for v4 in range(v1):
                for v5 in range(v2 - 2):
                    if abs(a1[v4][v5]) == abs(a1[v4][v5 + 1]) == abs(a1[v4][v5 + 2]) != 0:
                        a1[v4][v5] = a1[v4][v5 + 1] = a1[v4][v5 + 2] = -abs(a1[v4][v5])
                        v3 = True
            for v4 in range(v1 - 2):
                for v5 in range(v2):
                    if abs(a1[v4][v5]) == abs(a1[v4 + 1][v5]) == abs(a1[v4 + 2][v5]) != 0:
                        a1[v4][v5] = a1[v4 + 1][v5] = a1[v4 + 2][v5] = -abs(a1[v4][v5])
                        v3 = True
            for v5 in range(v2):
                v6 = v1 - 1
                for v4 in reversed(range(v1)):
                    if a1[v4][v5] > 0:
                        a1[v6][v5] = a1[v4][v5]
                        v6 -= 1
                for v4 in reversed(range(v6 + 1)):
                    a1[v4][v5] = 0
        return a1
