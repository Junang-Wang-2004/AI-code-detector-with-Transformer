import bisect

class C1(object):

    def maximumBeauty(self, a1, a2, a3, a4, a5):
        """
        """
        a1.sort()
        v1 = bisect.bisect_left(a1, a3)
        v2, v3 = (0, sum((a1[i] for v4 in range(v1))))
        v5 = v6 = 0
        for v7 in range(v1 + 1):
            if v7:
                v3 -= a1[v7 - 1]
            v8 = a2 - ((v1 - v7) * a3 - v3)
            if v8 < 0:
                continue
            while not (v6 == v7 or (v6 and (v8 + v2) // v6 <= a1[v6])):
                v2 += a1[v6]
                v6 += 1
            v9 = min((v8 + v2) // v6 if v6 else 0, a3 - 1)
            v5 = max(v5, v9 * a5 + (len(a1) - v7) * a4)
        return v5
