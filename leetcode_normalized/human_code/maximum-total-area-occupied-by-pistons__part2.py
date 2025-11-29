import collections
import itertools

class C1(object):

    def maxArea(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(int)
        for v2, v3 in zip(a3, a2):
            if v2 == 'U':
                v1[a1 - v3] -= 1
                v1[a1 - v3 + a1] += 1
            else:
                v1[v3] += 1
                v1[v3 + a1] -= 1
        v4 = v5 = sum(a2)
        v6 = a3.count('U')
        v7 = 0
        for v8, v2 in sorted(v1.items()):
            v5 += (v8 - v7) * (-(len(a3) - v6) + v6)
            v4 = max(v4, v5)
            v6 += v2
            v7 = v8
        return v4
