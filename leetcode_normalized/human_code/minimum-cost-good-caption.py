class C1(object):

    def minCostGoodCaption(self, a1):
        """
        """
        v1 = 3
        v2 = len(a1)
        if v2 < v1:
            return ''
        v3 = [[[0] * 2 for v4 in range(26)] for v4 in range(v2 - v1 + 1)]
        v5 = [[0] * 2 for v4 in range(v2 - v1 + 1)]
        v6 = [ord(x) - ord('a') for v7 in a1]
        for v8 in reversed(range(v2 - v1 + 1)):
            for v9 in range(26):
                if v8 == v2 - v1:
                    v3[v8][v9][:] = [sum((abs(v6[k] - v9) for v10 in range(v8, v8 + v1))), v1]
                    continue
                v3[v8][v9][:] = [v3[v8 + 1][v9][0] + abs(v6[v8] - v9), 1]
                if v8 + v1 < v2 - 2:
                    v11, v12 = v5[v8 + v1]
                    v11 += sum((abs(v6[v10] - v9) for v10 in range(v8, v8 + v1)))
                    if v11 < v3[v8][v9][0] or (v11 == v3[v8][v9][0] and v12 < v9):
                        v3[v8][v9][:] = [v11, v1]
            v5[v8] = min(([v3[v8][v9][0], v9] for v9 in range(26)))
        v13 = []
        v8, v9, v14 = (0, v5[0][1], 1)
        while v8 != v2:
            if v14 == v1:
                v9 = v5[v8][1]
            v14 = v3[v8][v9][1]
            v13.append(chr(ord('a') + v9) * v14)
            v8 += v14
        return ''.join(v13)
