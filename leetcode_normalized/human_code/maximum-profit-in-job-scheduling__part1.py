import itertools
import bisect

class C1(object):

    def jobScheduling(self, a1, a2, a3):
        """
        """
        v1 = sorted(zip(a2, a1, a3))
        v2 = [(0, 0)]
        for v3, v4, v5 in v1:
            v6 = bisect.bisect_right(v2, (v4 + 1, 0)) - 1
            if v2[v6][1] + v5 > v2[-1][1]:
                v2.append((v3, v2[v6][1] + v5))
        return v2[-1][1]
