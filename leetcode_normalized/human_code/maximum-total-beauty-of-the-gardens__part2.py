import bisect

class C1(object):

    def maximumBeauty(self, a1, a2, a3, a4, a5):
        """
        """
        a1.sort()
        v1 = bisect.bisect_left(a1, a3)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = v5 = 0
        v6 = v1
        for v7 in reversed(range(v1 + 1)):
            if v7 != v1:
                v5 += a1[v7]
            v8 = a2 - ((v1 - v7) * a3 - v5)
            if v8 < 0:
                continue
            v6 = min(v6, v7)
            while not (v6 == 0 or (v2[v6] - v2[v6 - 1]) * v6 - v2[v6] <= v8):
                v6 -= 1
            v9 = min((v8 + v2[v6]) // v6 if v6 else 0, a3 - 1)
            v4 = max(v4, v9 * a5 + (len(a1) - v7) * a4)
        return v4
