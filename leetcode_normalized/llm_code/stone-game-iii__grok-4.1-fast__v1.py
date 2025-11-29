class C1(object):

    def stoneGameIII(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1 - 1, -1, -1):
            v4 = float('-inf')
            v5 = 0
            for v6 in range(1, min(3, v1 - v3) + 1):
                v5 += a1[v3 + v6 - 1]
                v4 = max(v4, v5 - v2[v3 + v6])
            v2[v3] = v4
        v7 = v2[0]
        if v7 > 0:
            return 'Alice'
        elif v7 < 0:
            return 'Bob'
        else:
            return 'Tie'
