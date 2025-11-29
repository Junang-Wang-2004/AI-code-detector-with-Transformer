class C1(object):

    def numberOfWays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = abs(a2 - a1)
        if a3 < v2 or (a3 - v2) % 2 != 0:
            return 0
        v3 = (a3 - v2) // 2
        v4 = 1
        for v5 in range(1, v3 + 1):
            v4 = v4 * (a3 - v5 + 1) % v1
            v4 = v4 * pow(v5, v1 - 2, v1) % v1
        return v4
