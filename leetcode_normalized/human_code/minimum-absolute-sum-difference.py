import bisect

class C1(object):

    def minAbsoluteSumDiff(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = sorted(a1)
        v3 = v4 = 0
        for v5 in range(len(a2)):
            v6 = abs(a1[v5] - a2[v5])
            v3 = (v3 + v6) % v1
            if v6 < v4:
                continue
            v7 = bisect.bisect_left(v2, a2[v5])
            if v7 != len(v2):
                v4 = max(v4, v6 - abs(v2[v7] - a2[v5]))
            if v7 != 0:
                v4 = max(v4, v6 - abs(v2[v7 - 1] - a2[v5]))
        return (v3 - v4) % v1
