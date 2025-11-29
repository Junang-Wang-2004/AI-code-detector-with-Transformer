import itertools
import bisect

class C1(object):

    def minimumDifference(self, a1):
        """
        """
        v1, v2 = (a1[:len(a1) // 2], a1[len(a1) // 2:])
        v3, v4 = (sum(v1), sum(v2))
        v5 = float('inf')
        for v6 in range(len(v1) + 1):
            v7 = sorted((2 * sum(comb) - v3 for v8 in itertools.combinations(v1, v6)))
            for v8 in itertools.combinations(v2, len(v1) - v6):
                v9 = 2 * sum(v8) - v4
                v10 = bisect.bisect_left(v7, -v9)
                if v10 < len(v7):
                    v5 = min(v5, abs(v7[v10] + v9))
                if v10 > 0:
                    v5 = min(v5, abs(v7[v10 - 1] + v9))
        return v5
