import collections

class C1(object):

    def countTrapezoids(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = collections.defaultdict(int)
        for v3, v4 in a1:
            v2[v4] += 1
        v5 = v6 = 0
        for v7 in v2.values():
            v8 = v7 * (v7 - 1) // 2 % v1
            v5 = (v5 + v6 * v8 % v1) % v1
            v6 = (v6 + v8) % v1
        return v5
