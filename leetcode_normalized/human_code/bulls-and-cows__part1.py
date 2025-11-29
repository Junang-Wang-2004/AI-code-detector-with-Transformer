import operator
from collections import defaultdict, Counter

class C1(object):

    def getHint(self, a1, a2):
        """
        """
        v1, v2 = (0, 0)
        v3 = defaultdict(int)
        for v4, v5 in zip(a1, a2):
            if v4 == v5:
                v1 += 1
            else:
                v2 += int(v3[v4] < 0) + int(v3[v5] > 0)
                v3[v4] += 1
                v3[v5] -= 1
        return '%dA%dB' % (v1, v2)
