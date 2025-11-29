import bisect

class C1(object):

    def minimumMountainRemovals(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = []
        for v3 in range(len(a1) - 1):
            v4 = bisect.bisect_left(v2, a1[v3])
            if v4 == len(v2):
                v2.append(a1[v3])
            else:
                v2[v4] = a1[v3]
            v1[v3] = v4
        v5 = 0
        v2 = []
        for v3 in reversed(range(1, len(a1))):
            v4 = bisect.bisect_left(v2, a1[v3])
            if v4 == len(v2):
                v2.append(a1[v3])
            else:
                v2[v4] = a1[v3]
            if v3 < len(a1) - 1:
                v5 = max(v5, v1[v3] + v4)
        return len(a1) - (1 + v5)
