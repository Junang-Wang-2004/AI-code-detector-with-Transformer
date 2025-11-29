class C1(object):

    def countCells(self, a1, a2):
        """
        """

        def z_function(a1):
            v1 = [0] * len(a1)
            v2, v3 = (0, 0)
            for v4 in range(1, len(v1)):
                if v4 <= v3:
                    v1[v4] = min(v3 - v4 + 1, v1[v4 - v2])
                while v4 + v1[v4] < len(v1) and a1[v1[v4]] == a1[v4 + v1[v4]]:
                    v1[v4] += 1
                if v4 + v1[v4] - 1 > v3:
                    v2, v3 = (v4, v4 + v1[v4] - 1)
            return v1

        def check(a1):
            v1, v2 = (len(a1), len(a1[0]))
            if not a1:
                v1, v2 = (v2, v1)
            v3 = len(a2)
            v4 = list(a2)
            if a1:
                v4.extend((a1[i][j] for v5 in range(v1) for v6 in range(v2)))
            else:
                v4.extend((a1[v6][v5] for v5 in range(v1) for v6 in range(v2)))
            v7 = [[False] * v2 for v8 in range(v1)]
            v9 = z_function(v4)
            v10 = 0
            for v5 in range(v3, len(v4)):
                if v9[v5] < v3:
                    continue
                v10 = max(v10, v5 - v3)
                while v10 <= v5 - v3 + v3 - 1:
                    v7[v10 // v2][v10 % v2] = True
                    v10 += 1
            return v7
        v1 = check(True)
        v2 = check(False)
        return sum((v1[i][j] and v2[j][i] for v3 in range(len(a1)) for v4 in range(len(a1[0]))))
