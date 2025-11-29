import collections

class C1(object):

    def specialTriplets(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = collections.defaultdict(int)
        for v4 in a1:
            v3[v4] += 1
        v5 = collections.defaultdict(int)
        for v4 in a1:
            v3[v4] -= 1
            if not v3[v4]:
                del v3[v4]
            if 2 * v4 in v5 and 2 * v4 in v3:
                v2 = (v2 + v5[2 * v4] * v3[2 * v4]) % v1
            v5[v4] += 1
        return v2
