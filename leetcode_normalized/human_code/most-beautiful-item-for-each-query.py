import bisect

class C1(object):

    def maximumBeauty(self, a1, a2):
        """
        """
        a1.sort()
        for v1 in range(len(a1) - 1):
            a1[v1 + 1][1] = max(a1[v1 + 1][1], a1[v1][1])
        v2 = []
        for v3 in a2:
            v1 = bisect.bisect_left(a1, [v3 + 1])
            v2.append(a1[v1 - 1][1] if v1 else 0)
        return v2
