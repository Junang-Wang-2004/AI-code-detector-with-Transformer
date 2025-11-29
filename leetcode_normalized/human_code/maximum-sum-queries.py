import itertools
import bisect

class C1(object):

    def maximumSumQueries(self, a1, a2, a3):
        """
        """
        v1 = sorted(((i, j) for v2, v3 in zip(a1, a2)))
        v4 = [0] * len(a3)
        v5 = []
        for v6, v7, v2 in sorted(((v6, v7, v2) for v2, (v6, v7) in enumerate(a3)), reverse=True):
            while v1 and v1[-1][0] >= v6:
                v8, v9 = v1.pop()
                while v5 and v5[-1][1] <= v8 + v9:
                    v5.pop()
                if not v5 or v5[-1][0] < v9:
                    v5.append((v9, v8 + v9))
            v3 = bisect.bisect_left(v5, (v7,))
            v4[v2] = v5[v3][1] if v3 != len(v5) else -1
        return v4
