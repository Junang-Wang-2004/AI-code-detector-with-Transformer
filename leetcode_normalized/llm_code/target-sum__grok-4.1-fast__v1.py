class C1(object):

    def findTargetSumWays(self, a1, a2):
        v1 = sum(a1)
        if abs(a2) > v1 or (a2 + v1) % 2 != 0:
            return 0
        v2 = (a2 + v1) // 2
        v3 = [0] * (v2 + 1)
        v3[0] = 1
        for v4 in a1:
            for v5 in range(v2, v4 - 1, -1):
                v3[v5] += v3[v5 - v4]
        return v3[v2]
