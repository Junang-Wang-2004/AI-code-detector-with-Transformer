from functools import reduce

class C1(object):

    def numberOfWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a1 + 1)
        v2[0] = 1
        for v3 in (1, 2, 6):
            for v4 in range(v3, a1 + 1):
                v2[v4] += v2[v4 - v3]
        return reduce(lambda x, y: (x + v2[a1 - 4 * y]) % v1, (v3 for v3 in range(min(a1 // 4, 2) + 1)), 0)
