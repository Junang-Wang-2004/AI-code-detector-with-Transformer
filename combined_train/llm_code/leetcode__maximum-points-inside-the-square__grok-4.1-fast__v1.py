class C1(object):

    def maxPointsInsideSquare(self, a1, a2):
        v1 = float('inf')
        v2 = [v1] * 26
        v3 = [v1] * 26
        v4 = len(a1)
        for v5 in range(v4):
            v6, v7 = a1[v5]
            v8 = max(abs(v6), abs(v7))
            v9 = ord(a2[v5]) - ord('a')
            if v8 < v2[v9]:
                v3[v9] = v2[v9]
                v2[v9] = v8
            elif v8 < v3[v9]:
                v3[v9] = v8
        v10 = v1
        for v11 in range(26):
            if v3[v11] < v1:
                v10 = min(v10, v3[v11])
        v12 = 0
        for v11 in range(26):
            if v2[v11] < v10:
                v12 += 1
        return v12
