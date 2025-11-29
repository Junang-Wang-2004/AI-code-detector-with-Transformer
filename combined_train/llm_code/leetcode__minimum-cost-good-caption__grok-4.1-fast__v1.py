class C1(object):

    def minCostGoodCaption(self, a1):
        v1 = 3
        v2 = len(a1)
        if v2 < v1:
            return ''
        v3 = [ord(ch) - ord('a') for v4 in a1]
        v5 = v2 - v1 + 1
        v6 = [[0] * 26 for v7 in range(v5)]
        v8 = [[0] * 26 for v7 in range(v5)]
        v9 = [[0, 0] for v7 in range(v5)]
        for v10 in range(v5 - 1, -1, -1):
            if v10 == v5 - 1:
                for v11 in range(26):
                    v12 = sum((abs(v3[k] - v11) for v13 in range(v10, v10 + v1)))
                    v6[v10][v11] = v12
                    v8[v10][v11] = v1
                v9[v10] = min(((v6[v10][v11], v11) for v11 in range(26)))
                continue
            for v11 in range(26):
                v14 = abs(v3[v10] - v11) + v6[v10 + 1][v11]
                v6[v10][v11] = v14
                v8[v10][v11] = 1
                if v10 + v1 < v2 - 2:
                    v15, v16 = v9[v10 + v1]
                    v17 = v15 + sum((abs(v3[v13] - v11) for v13 in range(v10, v10 + v1)))
                    if v17 < v6[v10][v11] or (v17 == v6[v10][v11] and v16 < v11):
                        v6[v10][v11] = v17
                        v8[v10][v11] = v1
            v9[v10] = min(((v6[v10][v11], v11) for v11 in range(26)))
        v18 = []
        v19 = 0
        v20 = v9[0][1]
        v21 = 1
        while v19 != v2:
            if v21 == v1:
                v20 = v9[v19][1]
            v21 = v8[v19][v20]
            v18.append(chr(ord('a') + v20) * v21)
            v19 += v21
        return ''.join(v18)
