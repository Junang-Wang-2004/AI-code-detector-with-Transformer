import collections

class C1(object):

    def largestMultipleOfThree(self, a1):
        """
        """
        v1 = {0: [], 1: [(1,), (4,), (7,), (2, 2), (5, 2), (5, 5), (8, 2), (8, 5), (8, 8)], 2: [(2,), (5,), (8,), (1, 1), (4, 1), (4, 4), (7, 1), (7, 4), (7, 7)]}
        v2 = collections.Counter(a1)
        for v3 in v1[sum(a1) % 3]:
            v4 = collections.Counter(v3)
            if all((v2[k] >= v for v5, v6 in v4.items())):
                for v5, v6 in v4.items():
                    v2[v5] -= v6
                break
        v7 = ''.join((str(d) * v2[d] for v8 in reversed(range(10))))
        return '0' if v7 and v7[0] == '0' else v7
