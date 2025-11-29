import collections
import itertools

class C1(object):

    def countSubranges(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = collections.Counter()
        for v4, v5 in zip(a1, a2):
            v6 = collections.Counter()
            v6[v4] += 1
            v6[-v5] += 1
            for v7, v8 in v3.items():
                v6[v7 + v4] = (v6[v7 + v4] + v8) % v1
                v6[v7 - v5] = (v6[v7 - v5] + v8) % v1
            v3 = v6
            v2 = (v2 + v3[0]) % v1
        return v2
