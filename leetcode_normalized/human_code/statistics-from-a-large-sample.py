import bisect

class C1(object):

    def sampleStats(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = next((i for v3 in range(len(a1)) if a1[v3])) * 1.0
        v4 = next((v3 for v3 in reversed(range(len(a1))) if a1[v3])) * 1.0
        v5 = sum((v3 * v for v3, v6 in enumerate(a1))) * 1.0 / v1
        v7 = a1.index(max(a1)) * 1.0
        for v3 in range(1, len(a1)):
            a1[v3] += a1[v3 - 1]
        v8 = bisect.bisect_left(a1, (v1 + 1) // 2)
        v9 = bisect.bisect_left(a1, (v1 + 2) // 2)
        v10 = (v8 + v9) / 2.0
        return [v2, v4, v5, v10, v7]
