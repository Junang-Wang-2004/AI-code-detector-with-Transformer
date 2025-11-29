import bisect

class C1(object):

    def maximumBeauty(self, a1, a2, a3, a4, a5):
        """
        """

        def check(a1, a2, a3):
            return a3 and (a2 + a1[a3]) // a3 <= a1[a3 + 1] - a1[a3]

        def binary_search(a1, a2, a3, a4):
            while a3 <= a4:
                v1 = a3 + (a4 - a3) // 2
                if check(a1, a2, v1):
                    a4 = v1 - 1
                else:
                    a3 = v1 + 1
            return a3
        a1.sort()
        v1 = bisect.bisect_left(a1, a3)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = sum((a1[v3] for v3 in range(v1)))
        v5 = v6 = 0
        for v7 in range(v1 + 1):
            if v7:
                v4 -= a1[v7 - 1]
            v8 = a2 - ((v1 - v7) * a3 - v4)
            if v8 < 0:
                continue
            v6 = binary_search(v2, v8, 0, v7 - 1)
            v9 = min((v8 + v2[v6]) // v6 if v6 else 0, a3 - 1)
            v5 = max(v5, v9 * a5 + (len(a1) - v7) * a4)
        return v5
