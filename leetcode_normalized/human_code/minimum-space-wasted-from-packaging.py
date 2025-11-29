import bisect

class C1(object):

    def minWastedSpace(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = float('inf')
        a1.sort()
        v3 = v2
        for v4 in a2:
            v4.sort()
            if v4[-1] < a1[-1]:
                continue
            v5 = v6 = 0
            for v7 in v4:
                v8 = bisect.bisect_right(a1, v7, v6)
                v5 += v7 * (v8 - v6)
                v6 = v8
            v3 = min(v3, v5)
        return (v3 - sum(a1)) % v1 if v3 != v2 else -1
