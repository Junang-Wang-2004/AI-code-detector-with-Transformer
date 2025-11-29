class C1:

    def maxArea(self, a1, a2, a3):
        v1 = len(a2)
        v2 = sum(a2)
        v3 = sum((1 for v4 in a3 if v4 == 'U'))
        v5 = []
        for v4, v6 in zip(a3, a2):
            if v4 == 'U':
                v7 = a1 - v6
                v5.append((v7, -1))
                v5.append((v7 + a1, 1))
            else:
                v7 = v6
                v5.append((v7, 1))
                v5.append((v7 + a1, -1))
        v5.sort()
        v8 = v2
        v9 = 0
        v10 = 0
        while v10 < len(v5):
            v11 = v5[v10][0]
            v12 = v11 - v9
            v13 = 2 * v3 - v1
            v2 += v12 * v13
            v8 = max(v8, v2)
            while v10 < len(v5) and v5[v10][0] == v11:
                v3 += v5[v10][1]
                v10 += 1
            v9 = v11
        return v8
