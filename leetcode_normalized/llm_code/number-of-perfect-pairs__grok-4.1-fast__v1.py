class C1(object):

    def perfectPairs(self, a1):
        v1 = sorted((abs(x) for v2 in a1))
        v3 = 0
        v4 = 0
        v5 = len(v1)
        for v6 in range(v5):
            while v1[v6] > 2 * v1[v4]:
                v4 += 1
            v3 += v6 - v4
        return v3
