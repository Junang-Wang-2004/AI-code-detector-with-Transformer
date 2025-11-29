class C1(object):

    def kConcatenationMaxSum(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        if v2 == 0:
            return 0
        v3 = sum(a1)
        v4 = v5 = a1[0]
        for v6 in range(1, v2):
            v4 = max(a1[v6], v4 + a1[v6])
            v5 = max(v5, v4)
        v7 = v5
        v8 = 0
        v9 = float('-inf')
        for v10 in a1:
            v8 += v10
            v9 = max(v9, v8)
        v11 = 0
        v12 = float('-inf')
        for v6 in range(v2 - 1, -1, -1):
            v11 += a1[v6]
            v12 = max(v12, v11)
        if a2 == 1:
            return max(v7, 0) % v1
        v13 = max(v7, v9 + v12)
        v14 = max(v13, 0) + max(0, a2 - 2) * max(v3, 0)
        return v14 % v1
