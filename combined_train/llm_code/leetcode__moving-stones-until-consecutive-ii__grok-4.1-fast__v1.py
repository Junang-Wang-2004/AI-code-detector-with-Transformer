class C1(object):

    def numMovesStonesII(self, a1):
        a1.sort()
        v1 = len(a1)
        v2 = a1[-1] - a1[1] - v1 + 2
        v3 = a1[-2] - a1[0] - v1 + 2
        v4 = max(v2, v3)
        v5 = v1
        v6 = 0
        for v7 in range(v1):
            while v6 < v1 and a1[v6] - a1[v7] + 1 <= v1:
                v6 += 1
            v8 = v6 - v7
            if v8 == 0:
                continue
            v9 = a1[v6 - 1] - a1[v7] + 1
            v10 = v1 - v8
            if v10 == 1 and v9 == v1 - 1:
                v5 = min(v5, 2)
            else:
                v5 = min(v5, v10)
        return [v5, v4]
